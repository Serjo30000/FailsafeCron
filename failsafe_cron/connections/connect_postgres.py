import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ConnectPostgres:
    def __init__(self):
        self.load_env()

    def load_env(self):
        env_path = os.path.join(os.path.dirname(__file__), '..', '..', 'app.env')
        load_dotenv(env_path)

    def connect(self):
        db_uri = f"postgresql://{os.getenv('PYTHON_DATASOURCE_POSTGRES_USERNAME')}:{os.getenv('PYTHON_DATASOURCE_POSTGRES_PASSWORD')}@{os.getenv('PYTHON_DATASOURCE_POSTGRES_HOST')}/{os.getenv('PYTHON_DATASOURCE_POSTGRES_DB')}"
        self.engine = create_engine(db_uri)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session

    def get_engine(self):
        return self.engine