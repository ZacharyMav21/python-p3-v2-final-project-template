import click
from helpers import create_anime, delete_anime, display_all_anime, find_anime_by_id, create_episode, delete_episode, display_all_episodes, find_episode_by_id

@click.group()
def cli():
    """Anime Episode Tracker CLI"""
    pass

# Anime Menu
@cli.command()
def anime_menu():
    """Anime Menu options"""
    click.echo("Anime Menu:")
    click.echo("1. Create a new anime")
    click.echo("2. Delete an anime by ID")
    click.echo("3. Display all anime")
    click.echo("4. Find an anime by ID")

    choice = input("Select an option: ")
    
    if choice == "1":
        title = input("Enter anime title: ")
        genre = input("Enter genre: ")
        release_year = input("Enter release year: ")
        create_anime(title, genre, release_year)
    elif choice == "2":
        anime_id = input("Enter the ID of the anime to delete: ")
        delete_anime(anime_id)
    elif choice == "3":
        display_all_anime()
    elif choice == "4":
        anime_id = input("Enter the ID of the anime to find: ")
        find_anime_by_id(anime_id)
    else:
        click.echo("Invalid choice.")

# Episode Menu
@cli.command()
def episode_menu():
    """Episode Menu options"""
    click.echo("Episode Menu:")
    click.echo("1. Create a new episode")
    click.echo("2. Delete an episode by ID")
    click.echo("3. Display all episodes")
    click.echo("4. Find an episode by ID")

    choice = input("Select an option: ")
    
    if choice == "1":
        title = input("Enter episode title: ")
        air_date = input("Enter air date (YYYY-MM-DD): ")
        anime_id = input("Enter the anime ID: ")
        create_episode(title, air_date, anime_id)
    elif choice == "2":
        episode_id = input("Enter the ID of the episode to delete: ")
        delete_episode(episode_id)
    elif choice == "3":
        display_all_episodes()
    elif choice == "4":
        episode_id = input("Enter the ID of the episode to find: ")
        find_episode_by_id(episode_id)
    else:
        click.echo("Invalid choice.")

if __name__ == "__main__":
    cli()

