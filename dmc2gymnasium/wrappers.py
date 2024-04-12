from gymnasium import core, spaces
from dm_control import suite, manipulation
from dm_env import specs
import numpy as np
import os

def _spec_to_box(spec, dtype=np.float32):
    def extract_min_max(s):
        assert s.dtype == np.float64 or s.dtype == np.float32
        dim = int(np.prod(s.shape))
        if type(s) == specs.Array:
            bound = np.inf * np.ones(dim, dtype=np.float32)
            return -bound, bound
        elif type(s) == specs.BoundedArray:
            zeros = np.zeros(dim, dtype=np.float32)
            return s.minimum + zeros, s.maximum + zeros
        else:
            raise NotImplementedError(f"Unsupported spec type: {type(s)}")
    
    mins, maxs = [], []

    for s in spec:
        mn, mx = extract_min_max(s)
        mins.append(mn)
        maxs.append(mx)
    
    low = np.concatenate(mins, axis=0).astype(dtype)
    high = np.concatenate(maxs, axis=0).astype(dtype)

    assert low.shape == high.shape

    return spaces.Box(low, high, dtype=dtype)

def _flatten_obs(obs):
    obs_pieces = []
    
    for v in obs.values():
        flat = np.array([v]) if np.isscalar(v) else v.ravel()
        obs_pieces.append(flat)
    
    return np.concatenate(obs_pieces, axis=0)

class DMCWrapper(core.Env):
    def __init__(
            self,
            domain_name,
            task_name,
            task_kwargs={},
            environment_kwargs={},
            rendering="egl",
            render_height=84,
            render_width=84,
            render_camera_id=0,
    ):

        assert rendering in ["glfw", "egl", "osmesa"]
        os.environ["MUJOCO_GL"] = rendering

        # Create Task
        if domain_name == "manipulation":
            self._env = manipulation.load(
                environment_name=task_name,
                seed=task_kwargs.get("random", 42),
            )
        else:
            self._env = suite.load(
                domain_name=domain_name,
                task_name=task_name,
                task_kwargs=task_kwargs,
                environment_kwargs=environment_kwargs
            )

        # Gymnasium Rendering
        self.render_mode = "rgb_array"
        self.render_height = render_height
        self.render_width = render_width
        self.render_camera_id = render_camera_id

        # true and normalized action spaces
        self._true_action_space = _spec_to_box([self._env.action_spec()], np.float32)
        self._norm_action_space = spaces.Box(
            low=-1.0,
            high=1.0,
            shape=self._true_action_space.shape,
            dtype=np.float32
        )

        self._observation_space = _spec_to_box(self._env.observation_spec().values())
        self._action_space = _spec_to_box([self._env.action_spec()])

        if "random" in task_kwargs:
            seed = task_kwargs["random"]
            self._observation_space.seed(seed)
            self._action_space.seed(seed)

    
    def __getattr__(self, name):
        return getattr(self._env, name)
    
    @property
    def observation_space(self):
        return self._observation_space

    @property
    def action_space(self):
        return self._action_space
    
    @property
    def reward_range(self):
        """ DeepMind Control Suite has a per-step reward range of (0, 1) """
        return 0, 1
    
    def step(self, action):
        if action.dtype.kind == "f":
            action = action.astype(np.float32)
        
        assert self._action_space.contains(action)
        
        info = {"internal_state": self._env.physics.get_state().copy()}  # internal state prior to step
        time_step = self._env.step(action)
        observation = _flatten_obs(time_step.observation)
        reward = time_step.reward
        terminated = False  # never reach a goal
        truncated = time_step.last()
        info["discount"] = time_step.discount
        
        return observation, reward, terminated, truncated, info
    
    def reset(self, seed=None, options=None):
        time_step = self._env.reset()
        observation = _flatten_obs(time_step.observation)
        info = {}
        return observation, info
    
    def render(self, height=None, width=None, camera_id=0):
        height = height or self.render_height
        width = width or self.render_width
        camera_id = camera_id or self.render_camera_id
        return self._env.physics.render(height=height, width=width, camera_id=camera_id)
