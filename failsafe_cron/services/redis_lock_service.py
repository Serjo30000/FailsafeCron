from failsafe_cron.connections.connect_redis import ConnectRedis
from failsafe_cron.repositories.info_data_repository import InfoDataRepository

class RedisLockService:
    def __init__(self):
        self.repository = InfoDataRepository()
        connect_redis = ConnectRedis()
        self.redis_template = connect_redis.connect()

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