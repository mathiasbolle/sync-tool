from dataclasses import dataclass
from dotenv import dotenv_values, load_dotenv
import logging

load_dotenv()
_config = dotenv_values()
logging.getLogger().setLevel(logging.INFO)

@dataclass
class SyncConfig:
    baseUrl: str = str(_config['BASE_URL'])

    masterClient: str = str(_config['MASTER_CLIENT'])
    masterSecret: str = str(_config['MASTER_SECRET'])

    targetClient: str = str(_config['TARGET_CLIENT'])
    targetSecret: str = str(_config['TARGET_SECRET'])

    cron: str = str(_config['CRON'])
