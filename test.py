from dmc2gymnasium import DMCWrapper
from gymnasium.wrappers.pixel_observation import PixelObservationWrapper


def main():

    env = DMCWrapper(domain_name="point_mass", task_name="easy")

    env = PixelObservationWrapper(env, pixels_only=False, render_kwargs={"pixels": {"height": 84, "width": 84}})

    observation, info = env.reset(seed=42)

    for step in range(1000):
        action = env.action_space.sample()

        observation, reward, terminated, truncated, info = env.step(action)

        state = observation["state"]
        pixels = observation["pixels"]

        print(state.shape, pixels.shape)

        if terminated or truncated:
            observation, info = env.reset(seed=42)

    env.close()


if __name__ == "__main__":
    main()
