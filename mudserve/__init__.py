from sqlalchemy.orm import sessionmaker
from mudserve.models.base import engine

dbsession = sessionmaker(bind=engine)
