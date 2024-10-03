from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connect to a local SQLite database
engine = create_engine('sqlite:///anime_tracker.db')

# Base class for our models
Base = declarative_base()

# Session setup
Session = sessionmaker(bind=engine)
session = Session()

# This function can be called to create tables
def create_tables():
    Base.metadata.create_all(engine)
