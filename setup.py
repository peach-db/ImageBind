from setuptools import setup

requirements = []

# Read requirements from files
with open("requirements.txt", "r") as f:
    requirements.extend(f.read().splitlines())

setup(
    name="imagebind",
    version="1.0.0",
    packages=["imagebind"],
    install_requires=requirements,
    dependency_links=["https://download.pytorch.org/whl/cu113"],
)
