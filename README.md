# dmc2gymnasium

This is a lightweight wrapper around the DeepMind Control Suite that provides the standard Farama Gymnasium interface to users. 

Farama Gymnasium is the continuation of OpenAI Gym, and this repository will provide users with a simple, up-to-date, and easy-to-install package for their DM Control Suite experiments.

## Usage

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

## References

This work is largely inspired by the following repos:

- imgeorgiev/dmc2gymnasium [[Link](https://github.com/imgeorgiev/dmc2gymnasium)]
- denisyarats/dmc2gym [[Link](https://github.com/denisyarats/dmc2gym)]
