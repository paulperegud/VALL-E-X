from setuptools import setup, find_packages

# Read dependencies from requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md", "r") as f:
    long_description = f.read()

packages = find_packages()
print(f"packages: {packages}")

setup(
    name="vall-e-x",
    python_requires=">=3.10.0",
    version="0.0.1",
    description="Open source implementation of Microsoft's [VALL-E X](https://arxiv.org/pdf/2303.03926) zero-shot TTS model",
    author="https://github.com/Plachtaa",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=packages,
    install_requires=required,
    url="https://github.com/Plachtaa/VALL-E-X",
)
