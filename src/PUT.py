import json
from sqlitedict import SqliteDict


def read_from_file(file_path: str) -> dict:
    with open(file_path) as my_file:
        data: dict = json.load(my_file)
    return data


def put_function(pair, file_path: str, db: SqliteDict):
    print("PUT ", pair, file_path)
    data: dict

    if file_path is not None:
        print("PUT FILE ", file_path)
        data = read_from_file(file_path)
    else:
        data = json.loads(pair)
