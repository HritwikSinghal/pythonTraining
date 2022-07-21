import json
from sqlitedict import SqliteDict


def del_function(key: str, db: SqliteDict):
    print("delete ", key)
