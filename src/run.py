import json

import click
import uvicorn

import client_test
from .base import Database, Server


# A very Poorly Optimized Key Value Store.DO NOT USE THIS

@click.command()
@click.option('-s', '--show', help='Show DB', is_flag=True)
@click.option('-g', '--get', help='Get the key from store', type=str)
@click.option('-p', '--put', help='Put the key in store. (like "X=5") ', type=str)
@click.option('-f', '--put_file_path', help='Put the key in store from a file.', type=str)
@click.option('-d', '--delete', help='Delete the key from store', type=str)
@click.option('-t', '--truncate', help='Show DB', is_flag=True)
@click.option('-d', '--db', help="DB file to read/write to/from.", type=str)
# @click.option('--client-file', help='start client app using the file specified', type=str)
@click.option('--client', help='start client app', is_flag=True)
@click.option('--server', help='start DB server', is_flag=True)
def start(get, put, put_file_path, delete, show, truncate, db, client, server) -> None:
    if server:
        # todo: get port from config file
        uvicorn.run(Server.app, host="127.0.0.1", port=8080, log_level="info")
    elif client:
        client_test.start()
    else:
        if not db:
            db = str
        my_db = Database.Database()

        if show:
            print(json.dumps(my_db.show(), indent=3))
        elif get:
            print(my_db.get(get))
        elif put:
            print(my_db.put(put))
        elif put_file_path:
            print(my_db.put_from_file(put_file_path))
        elif delete:
            print(my_db.delete(delete))
        elif truncate:
            print(my_db.truncate())
