from models import session, Anime, Episode

def create_anime(title, genre, release_year):
    anime = Anime(title=title, genre=genre, release_year=release_year)
    session.add(anime)
    session.commit()
    print(f"Anime '{title}' created successfully.")

def delete_anime(anime_id):
    anime = session.query(Anime).get(anime_id)
    if anime:
        session.delete(anime)
        session.commit()
        print(f"Anime with ID {anime_id} deleted successfully.")
    else:
        print(f"Anime with ID {anime_id} not found.")

def display_all_anime():
    animes = session.query(Anime).all()
    if animes:
        for anime in animes:
            print(f"ID: {anime.id}, Title: {anime.title}, Genre: {anime.genre}, Release Year: {anime.release_year}")
    else:
        print("No anime found.")

def find_anime_by_id(anime_id):
    anime = session.query(Anime).get(anime_id)
    if anime:
        print(f"ID: {anime.id}, Title: {anime.title}, Genre: {anime.genre}, Release Year: {anime.release_year}")
    else:
        print(f"Anime with ID {anime_id} not found.")

def create_episode(title, air_date, anime_id):
    anime = session.query(Anime).get(anime_id)
    if anime:
        episode = Episode(title=title, air_date=air_date, anime_id=anime_id)
        session.add(episode)
        session.commit()
        print(f"Episode '{title}' created successfully for anime '{anime.title}'.")
    else:
        print(f"Anime with ID {anime_id} not found.")

def delete_episode(episode_id):
    episode = session.query(Episode).get(episode_id)
    if episode:
        session.delete(episode)
        session.commit()
        print(f"Episode with ID {episode_id} deleted successfully.")
    else:
        print(f"Episode with ID {episode_id} not found.")

def display_all_episodes():
    episodes = session.query(Episode).all()
    if episodes:
        for episode in episodes:
            print(f"ID: {episode.id}, Title: {episode.title}, Air Date: {episode.air_date}, Anime ID: {episode.anime_id}")
    else:
        print("No episodes found.")

def find_episode_by_id(episode_id):
    episode = session.query(Episode).get(episode_id)
    if episode:
        print(f"ID: {episode.id}, Title: {episode.title}, Air Date: {episode.air_date}, Anime ID: {episode.anime_id}")
    else:
        print(f"Episode with ID {episode_id} not found.")
