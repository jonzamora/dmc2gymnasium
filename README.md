# dmc2gymnasium

This is a lightweight wrapper around the DeepMind Control Suite that provides the standard Farama Gymnasium interface to users. 

Farama Gymnasium is the continuation of OpenAI Gym, and this repository will provide users with a simple, up-to-date, and easy-to-install package for their DM Control Suite experiments.

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

env = DMCWrapper(domain_name="point_mass", task_name="easy")
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

## Notes:

I've mostly designed this for my own experiments, but feel free to use this if it applies to your work!

I plan to extend this to work with DeepMind Control's `manipulation` tasks, which can be found [here](https://github.com/google-deepmind/dm_control/tree/main/dm_control/manipulation)

## References

This work is largely inspired by the following repos:

- imgeorgiev/dmc2gymnasium [[Link](https://github.com/imgeorgiev/dmc2gymnasium)]
- denisyarats/dmc2gym [[Link](https://github.com/denisyarats/dmc2gym)]
