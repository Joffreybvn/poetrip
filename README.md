
# Poetrip

[![image](https://img.shields.io/pypi/v/poetrip.svg)](https://pypi.org/project/poetrip/)
[![image](https://img.shields.io/pypi/l/poetrip.svg)](https://pypi.org/project/poetrip/)
[![image](https://img.shields.io/pypi/pyversions/poetrip.svg)](https://pypi.org/project/poetrip/)

Generate Pipfile from pyproject.toml.

## Installation
Poetrip requires Python 3.6 or greater.

Using **pip**:
```Shell
pip install poetrip
```

Using **poetry**:
```shell
poetry add --dev poetrip
```

## CLI Quickstart
TODO

## API Quickstart
Get a Pipfile from a pyproject.toml:
```python
from poetrip import PyProject

# Load and transform
pyproject = PyProject.from_file("./pyproject.toml")
pipfile = pyproject.to_pipfile()

# Write to disk
pipfile.to_file("./Pipfile")
```
