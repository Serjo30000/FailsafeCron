import redis
from failsafe_cron.services.info_data_service import InfoDataService
from failsafe_cron.utils.StringUtil import StringUtil
import os
from dotenv import load_dotenv

class ScheduledService:
    def __init__(self):
        env_path = os.path.join(os.path.dirname(__file__), '..', '..', 'app.env')
        load_dotenv(env_path)
        self.service = InfoDataService()
        self.redis_template = redis.StrictRedis(os.getenv('PYTHON_DATA_REDIS_HOST'), os.getenv('PYTHON_DATA_REDIS_PORT'), os.getenv('PYTHON_DATA_REDIS_DB'))

    def script(self, data):
        StringUtil.print_number_of_models_before(self.service.number_of_models())
        lock = self.redis_template.getset("lock", "lock")
        self.redis_template.expire("lock", 15)
        if lock is None:
            StringUtil.print_lock()
            self.service.create_info_data(data)
        else:
            StringUtil.print_skip()

        StringUtil.print_number_of_models_after(self.service.number_of_models())