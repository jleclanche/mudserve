from mudserve.models.base import Base
from sqlalchemy import Column, String, Integer

class User(Base):
	__tablename__ = "users"
	
	id = Column(Integer, primary_key=True)
	email = Column(String(50))
	password = Column(String(30))
