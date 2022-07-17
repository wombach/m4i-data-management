from logging import warning
from typing import Any, Dict, Iterator

_instance: 'ConfigStore' = None


class MissingRequiredConfigException(Exception):
    pass


class ConfigStore():
    _config: Dict[str, Any] = {}

    @classmethod
    def get_instance(cls) -> 'ConfigStore':
        global _instance
        if not _instance:
            _instance = cls()
        # END IF
        return _instance

    # END get_instance

    @classmethod
    def initialize(cls, config: Dict[str, Any]) -> 'ConfigStore':
        if not _instance:
            instance = cls.get_instance()
            instance.load(config)
        # END IF
        return _instance

    # END get_instance

    def get(self, key: str, default: Any = None, required: bool = False) -> Any:
        if not key in self._config:
            if required and default is None:
                raise MissingRequiredConfigException(
                    f"Required Config value for key {{{key}}}, no default provided."
                )
            else:
                warning(
                    f"No value has been configured for key {{{key}}}. Returning the default value instead."
                )
        # END IF
        return self._config.get(key, default)

    # END get

    def get_many(self, *keys: str, defaults: Dict[str, Any] = None, required: Dict[str, Any] = None,
                 all_required: bool = False) -> Iterator[Any]:
        if defaults is None:
            defaults = {}
        if required is None:
            required = {}

        def resolver(key):
            return self.get(key, defaults.get(key), all_required or required.get(key))

        # END resolver

        return map(resolver, keys)

    # END get_many

    def load(self, config: Dict[str, Any]):
        self.set_many(**config)

    # END load

    def reset(self):
        self._config = {}

    # END reset

    def set(self, key: str, value: Any):
        self._config[key] = value

    # END set

    def set_many(self, **kwargs):
        for key, value in kwargs.items():
            self.set(key, value)
        # END LOOP
    # END set_many

# END ConfigStore
