from hashlib import md5
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from mudserve.models.base import Base
from mudserve.models.user import User

class Auth(Base):
	__tablename__ = "auth"
	
	auth_token = Column(String(40), primary_key=True)
	user_id = Column(Integer, ForeignKey("users.id"))
	expire_time = Column(DateTime, index=True)
	
	user = relationship(User, backref=backref("auth_set"))
	
