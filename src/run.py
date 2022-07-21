import click

from src import GET, PUT, DEL
from sqlitedict import SqliteDict

db = SqliteDict("my_db.sqlite")


@click.command()
@click.option('--get', help='Get the key from store', type=str)
@click.option('--put', help='Put the key in store.', type=str)
@click.option('--put_file_path', help='Put the key in store from a file.', type=str)
@click.option('--delete', help='Delete the key from store', type=str)
@click.option('--count', default=1, help='Number of greetings.', type=int)
@click.option('--name', default="Hritwik", help='The person to greet.', type=str)
def start(get, put, put_file_path, delete, count, name) -> None:
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

    if get is not None:
        GET.get_function(get, db)
    if put is not None:
        PUT.put_function(put, db)
    if put_file_path is not None:
        PUT.put_from_file(file_path=put_file_path, db=db),
    if delete is not None:
        DEL.del_function(delete, db)
