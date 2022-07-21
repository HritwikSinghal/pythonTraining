import click

from src import Database


@click.command()
@click.option('--get', help='Get the key from store', type=str)
@click.option('--put', help='Put the key in store.', type=str)
@click.option('--put_file_path', help='Put the key in store from a file.', type=str)
@click.option('--delete', help='Delete the key from store', type=str)
@click.option('--count', default=1, help='Number of greetings.', type=int)
@click.option('--name', default="Hritwik", help='The person to greet.', type=str)
def start(get, put, put_file_path, delete, count, name) -> None:
    for x in range(count):
        click.echo(f"Hello {name}!")

    my_db = Database()

    if get is not None:
        my_db.get(get)
    if put is not None:
        my_db.put(put)
    if put_file_path is not None:
        my_db.put_from_file(file_path=put_file_path)
    if delete is not None:
        my_db.delete(delete)
