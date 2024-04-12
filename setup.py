"""
setuptools script for dmc2gymnasium.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="dmc2gymnasium",  # Required
    version="1.0.0",  # Required
    description="DeepMind Control Suite to Farama Gymnasium Wrapper",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/jonzamora/dmc2gymnasium",  # Optional
    author="Jonathan Zamora",  # Optional
    author_email="jonathan.zamora@usc.edu",  # Optional
    keywords="dm_control, gymnasium, gym",  # Optional
    packages=find_packages(),  # Required
    install_requires=["gymnasium", "dm_control", "mujoco", "moviepy"],  # Optional
)
