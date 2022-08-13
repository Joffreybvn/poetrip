
<p align="center">
  <img src="./docs/logo.svg" alt="Poetrip">
</p>
<p align="center">
    <em>Generate Pipfile from pyproject.toml.</em>
</p>
<p align="center">
    <a href="https://pypi.org/project/poetrip/" target="_blank">
        <img src="https://img.shields.io/pypi/v/poetrip.svg" alt="Version">
    </a>
    <a href="https://pypi.org/project/poetrip/" target="_blank">
        <img src="https://img.shields.io/pypi/l/poetrip.svg" alt="License">
    </a>
    <a href="https://pypi.org/project/poetrip/" target="_blank">
        <img src="https://img.shields.io/pypi/pyversions/poetrip.svg" alt="Python">
    </a>
</p>

---

**Source Code**: [https://github.com/Joffreybvn/poetrip](https://github.com/Joffreybvn/poetrip)

**Pypi**: [https://pypi.org/project/poetrip/](https://pypi.org/project/poetrip/)

---

Poetrip is a small library and CLI to quickly create Pipfile from existing pyproject.toml.

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
Get a Pipfile from a pyproject.toml:
```shell
$ poetrip --from pyproject.toml --to Pipfile
```

Or simply:
```shell
$ poetrip
```
Takes the pyproject.toml in the current folder and generate a Pipfile.

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
