from sqlalchemy import Column, Integer, String, Date, ForeignKey
from .database import Base

class Episode(Base):
    __tablename__ = 'episode'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    air_date = Column(Date)
    anime_id = Column(Integer, ForeignKey('anime.id'))

    def __repr__(self):
        return f"<Episode(id={self.id}, title={self.title}, air_date={self.air_date}, anime_id={self.anime_id})>"
