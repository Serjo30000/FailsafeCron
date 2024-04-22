from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from failsafe_cron.models.info_data import InfoData, Base
import os
from dotenv import load_dotenv

class InfoDataRepository:
    def __init__(self):
        env_path = os.path.join(os.path.dirname(__file__), '..', '..', 'app.env')
        load_dotenv(env_path)

        db_uri = f"postgresql://{os.getenv('PYTHON_DATASOURCE_POSTGRES_USERNAME')}:{os.getenv('PYTHON_DATASOURCE_POSTGRES_PASSWORD')}@{os.getenv('PYTHON_DATASOURCE_POSTGRES_HOST')}/{os.getenv('PYTHON_DATASOURCE_POSTGRES_DB')}"

        self.engine = create_engine(db_uri)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def create(self, data):
        session = self.Session()
        session.add(data)
        session.commit()
        session.close()

    def read(self, id_):
        session = self.Session()
        data = session.query(InfoData).get(id_)
        session.close()
        return data

    def read_all(self):
        session = self.Session()
        data = session.query(InfoData).all()
        session.close()
        return data

    def update(self, id_, new_data):
        session = self.Session()
        data = session.query(InfoData).get(id_)
        if data:
            for attr, value in new_data.items():
                setattr(data, attr, value)
            session.commit()
        session.close()

    def delete(self, id_):
        session = self.Session()
        data = session.query(InfoData).get(id_)
        if data:
            session.delete(data)
            session.commit()
        session.close()