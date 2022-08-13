import toml
from typing import Dict, Any
from poetrip.pipfile import PipFile


class PyProject:

    def __init__(
            self,
            infos: dict = None,
            dependencies: dict = None,
            dev_dependencies: dict = None
    ):
        self._infos = infos or {}
        self._dependencies = dependencies or {}
        self._dev_dependencies = dev_dependencies or {}

    @classmethod
    def from_file(cls, filename: str = 'pyproject.toml') -> 'PyProject':
        """Load a PyProject file from a filename."""
        toml_content = dict(toml.load(filename))
        poetry_attributes: dict = toml_content['tool']['poetry']

        return cls(
            dependencies=poetry_attributes.pop('dependencies'),
            dev_dependencies=poetry_attributes.pop('dev-dependencies'),
            infos=poetry_attributes
        )

    @property
    def attributes(self) -> Dict[str, Any]:
        return {'tool': {'poetry': {
            **self._infos,
            'dependencies': self._dependencies,
            'dev-dependencies': self._dev_dependencies
        }}}

    def _get_requires(self) -> dict:
        python_version: str = self._dependencies.pop('python')
        return {'python-version': python_version}

    def to_pipfile(self) -> 'PipFile':
        return PipFile(
            requires=self._get_requires(),
            packages=self._dependencies,
            dev_packages=self._dev_dependencies
        )
