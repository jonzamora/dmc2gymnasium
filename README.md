# dmc2gymnasium

This is a lightweight wrapper around the **DeepMind Control Suite** and **DeepMind Robot Manipulation Tasks**, and provides the standard Farama Gymnasium API interface to users. 

Farama Gymnasium is the continuation of OpenAI Gym, and this repository will provide users with a simple, up-to-date, and easy-to-install package for their DM Control Suite experiments.

For a complete list of tasks, see the `dm_control` paper [here](https://arxiv.org/abs/2006.12983) and check out Part II of the Paper.

## Installation

```bash
git clone https://github.com/jonzamora/dmc2gymnasium
cd dmc2gymnasium
pip install -e .
```

## Usage

A complete usage of the DMCWrapper is as follows:

```python
from dmc2gymnasium import DMCWrapper

env = DMCWrapper(domain_name="manipulation", task_name="place_brick_features")
observation, info = env.reset(seed=42)

for step in range(1000):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset(seed=42)

env.close()
```

If you'd like to test this out, simply run the following:

```bash
python test.py
```

Output will look like this in the `video` directory:

https://github.com/jonzamora/dmc2gymnasium/assets/50164418/7a6dead7-6b09-4ef4-8a5d-71bb0190ccbe

## Notes

I've mostly designed this for my own experiments, but feel free to use this if it applies to your work!

If you have a feature request, or encounter any problems, please make an Issue [here](https://github.com/jonzamora/dmc2gymnasium/issues) and i'm happy to discuss further.

## References

This work is **largely** inspired by the following repos:

- imgeorgiev/dmc2gymnasium [[Link](https://github.com/imgeorgiev/dmc2gymnasium)]
- denisyarats/dmc2gym [[Link](https://github.com/denisyarats/dmc2gym)]
