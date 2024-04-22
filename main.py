from flask import Flask

from failsafe_cron.models.info_data import InfoData
from failsafe_cron.services.scheduled_service import ScheduledService

app = Flask(__name__)

scheduled_service = ScheduledService()

def run_script():
    new_data = InfoData(name='Name', description='Description', date_created='2024-04-20')
    scheduled_service.script(new_data)

if __name__ == '__main__':
    run_script()
    app.run(debug=True)

