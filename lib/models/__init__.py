from .database import session, create_tables
from .anime import Anime
from .episode import Episode

# Create the tables if they don't already exist in the database
create_tables()

# Expose the session, Anime, and Episode models for use in other parts of the app
__all__ = ['session', 'Anime', 'Episode']
