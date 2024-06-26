"""
This script demonstrates how to use the DMCWrapper
"""

from dmc2gymnasium import DMCWrapper
from gymnasium.wrappers.pixel_observation import PixelObservationWrapper
from gymnasium.wrappers.record_video import RecordVideo


def main():

    task_kwargs = {"random": 42}

    env = DMCWrapper(domain_name="manipulation", task_name="place_brick_features", render_height=256, render_width=256, task_kwargs=task_kwargs)
    env = PixelObservationWrapper(env, pixels_only=False, render_kwargs={"pixels": {"height": 256, "width": 256}})
    env = RecordVideo(env, video_folder="video", step_trigger=lambda x: x % 1000 == 0)

    observation, info = env.reset(seed=42)

    for step in range(1000):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset(seed=42)

    env.close()


if __name__ == "__main__":
    main()
