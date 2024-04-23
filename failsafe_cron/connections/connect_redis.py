import os

import redis
from dotenv import load_dotenv

class ConnectRedis:
    def __init__(self):
        self.load_env()

    def load_env(self):
        env_path = os.path.join(os.path.dirname(__file__), '..', '..', 'app.env')
        load_dotenv(env_path)

    def connect(self):
        return redis.StrictRedis(os.getenv('PYTHON_DATA_REDIS_HOST'), os.getenv('PYTHON_DATA_REDIS_PORT'), os.getenv('PYTHON_DATA_REDIS_DB'))