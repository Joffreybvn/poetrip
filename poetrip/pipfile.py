import toml
from typing import Dict, Any


class PipFile:

    _SOURCE_DEFAULT: Dict[str, str] = {
        "url": "https://pypi.org/simple",
        "verify_ssl": True,
        "name": "pypi"
    }

    def __init__(
            self,
            source: dict = None,
            requires: dict = None,
            packages: dict = None,
            dev_packages: dict = None
    ):
        self._source: dict = source or self._SOURCE_DEFAULT
        self._requires: dict = requires or {}
        self._packages: dict = packages or {}
        self._dev_packages: dict = dev_packages or {}

    @property
    def attributes(self) -> Dict[str, Any]:
        return {
            'source': [self._source],
            'requires': self._requires,
            'packages': self._packages,
            'dev-packages': self._dev_packages
        }

    def to_file(self, filename: str = 'Pipfile') -> None:
        """Create a Pipfile on disk."""
        with open(filename, 'w') as file:
            toml.dump(self.attributes, file)
