import click

from src import Database


# A very Poorly Optimized Key Value Store.DO NOT USE THIS

@click.command()
@click.option('-g', '--get', help='Get the key from store', type=str)
@click.option('-p', '--put', help='Put the key in store. (like "X=5") ', type=str)
@click.option('-f', '--put_file_path', help='Put the key in store from a file.', type=str)
@click.option('-d', '--delete', help='Delete the key from store', type=str)
@click.option('-s', '--show', help='Show DB', is_flag=True)
def start(get, put, put_file_path, delete, show) -> None:
    my_db = Database.Database()

    if show:
        my_db.show_db()
    if get is not None:
        my_db.get(get)
    if put is not None:
        my_db.put(put)
    if put_file_path is not None:
        my_db.put_from_file(file_path=put_file_path)
    if delete is not None:
        my_db.delete(delete)
