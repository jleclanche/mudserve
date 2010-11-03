# Database configuration
from mudserve.settings import DATABASE
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("%(type)s://%(username)s:%(password)s@%(hostname)s:%(port)d/%(database)s" % DATABASE)
Base = declarative_base(bind=engine)
