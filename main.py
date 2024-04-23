from flask import Flask

from failsafe_cron.models.info_data import InfoData
from failsafe_cron.services.redis_lock_service import RedisLockService

app = Flask(__name__)

redis_lock_service = RedisLockService()

def run_script():
    new_data = InfoData(name='Name', description='Description', date_created='2024-04-20')
    redis_lock_service.script(new_data)

if __name__ == '__main__':
    run_script()
    app.run(debug=True)

