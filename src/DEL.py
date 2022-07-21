import os
import json


def del_function(key: str, db: dict):
    print("delete ", key)
    db.pop(key, None)
    with open(os.environ.get('db')) as my_file:
        json.dump(db, my_file)
