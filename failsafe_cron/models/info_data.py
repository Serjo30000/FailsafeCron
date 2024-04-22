from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class InfoData(Base):
    __tablename__ = 'info_datas'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    date_created = Column(Date)