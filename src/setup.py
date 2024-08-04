from setuptools import setup, find_packages

setup(
    name="luxai-s3",
    version="0.1.0",
    packages=find_packages(exclude="kits"),
    install_requires=[
        "jax",
        "gymnax==0.0.8",
    ],
    author="Lux AI Challenge",
    description="Lux AI Challenge Season 3 environment code",
    long_description=open("../README.md").read(),
    long_description_content_type="text/markdown",
)