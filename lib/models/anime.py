from sqlalchemy import Column, Integer, String
from .database import Base

class Anime(Base):
    __tablename__ = 'anime'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)
    release_year = Column(Integer)

    def __repr__(self):
        return f"<Anime(id={self.id}, title={self.title}, genre={self.genre}, release_year={self.release_year})>"
