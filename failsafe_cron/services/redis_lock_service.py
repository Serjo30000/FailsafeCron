import redis

from failsafe_cron.repositories.info_data_repository import InfoDataRepository
import os
from dotenv import load_dotenv

class RedisLockService:
    def __init__(self):
        env_path = os.path.join(os.path.dirname(__file__), '..', '..', 'app.env')
        load_dotenv(env_path)
        self.repository = InfoDataRepository()
        self.redis_template = redis.StrictRedis(os.getenv('PYTHON_DATA_REDIS_HOST'), os.getenv('PYTHON_DATA_REDIS_PORT'), os.getenv('PYTHON_DATA_REDIS_DB'))

    def script(self, data):
        print("Number of models in database before script:", len(self.repository.read_all()))
        lock = self.redis_template.getset("lock", "lock")
        self.redis_template.expire("lock", 15)
        if lock is None:
            print("\nLOCK\n")
            self.repository.create(data)
        else:
            print("\nSKIP\n")

        print("Number of models in database after script:", len(self.repository.read_all()))