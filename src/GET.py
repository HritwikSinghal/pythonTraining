import json
from sqlitedict import SqliteDict


def get_function(key: str, db: SqliteDict):
    print("get", key)
