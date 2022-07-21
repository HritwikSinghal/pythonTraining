import json
import os


def read_from_file(file_path: str) -> dict:
    with open(file_path) as my_file:
        data: dict = json.load(my_file)
    return data


def put_from_file(file_path: str, db: dict):
    data = read_from_file(file_path)
    db = db | data

    with open(os.environ.get('db')) as my_file:
        json.dump(db, my_file)


def put_function(pair, db: dict):
    print("PUT ", pair)

    data: dict = json.loads(pair)
    # todo: complete this

    db = db | data
    with open(os.environ.get('db')) as my_file:
        json.dump(db, my_file)
