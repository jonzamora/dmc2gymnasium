"""
setuptools script for dmc2gymnasium.
"""


from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="dmc2gymnasium",
    version="1.0.0",
    description="Farama Gymnasium API Wrapper for DeepMind Control Suite",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonzamora/dmc2gymnasium",
    author="Jonathan Zamora",
    author_email="jonathan.zamora@usc.edu",
    keywords="dm_control, gymnasium, gym",
    packages=find_packages(),
    install_requires=["gymnasium", "dm_control", "mujoco", "moviepy"],
)
