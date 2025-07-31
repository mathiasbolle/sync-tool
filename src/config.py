from dataclasses import dataclass
from dotenv import dotenv_values, load_dotenv
import logging

load_dotenv()
_config = dotenv_values()
logging.getLogger().setLevel(logging.INFO)

class SyncConfigSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

@dataclass(frozen=True)
class SyncConfig(metaclass=SyncConfigSingleton):
    baseUrl: str = str(_config['BASE_URL'])

    masterClient: str = str(_config['MASTER_CLIENT'])
    masterSecret: str = str(_config['MASTER_SECRET'])

    targetClient: str = str(_config['TARGET_CLIENT'])
    targetSecret: str = str(_config['TARGET_SECRET'])

    cron: str = str(_config['CRON'])
