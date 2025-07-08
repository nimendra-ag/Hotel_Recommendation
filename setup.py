from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="Hotel_Recommendation",
    version="0.1",
    author="Nimendra",
    packages=find_packages(),
    install_requires=requirements,
)