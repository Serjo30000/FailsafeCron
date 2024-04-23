from failsafe_cron.connections.connect_postgres import ConnectPostgres
from failsafe_cron.models.info_data import InfoData, Base

class InfoDataRepository:
    def __init__(self):
        connect_postgres = ConnectPostgres()
        connect_postgres.connect()
        Base.metadata.create_all(connect_postgres.get_engine())
        self.Session = connect_postgres.get_session()

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