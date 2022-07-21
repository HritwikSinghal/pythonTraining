import json
from pathlib import Path


class Database:

    def __init__(self):
        self.db_location = "my_db.db"
        with open(self.db_location, 'w+') as my_db:
            my_db.write("{}")
            self.db: dict = json.load(my_db)

    def __int__(self, location: str):
        self.db_location = location
        with open(self.db_location) as my_db:
            self.db: dict = json.load(my_db)

    def write_db_to_file(self) -> None:
        with open(self.db_location, 'r+') as my_file:
            json.dump(self.db, my_file)

    def read_file(self, location) -> dict:
        with open(location) as my_file:
            data: dict = json.load(my_file)
        return data

    ### --------------------------------------------------------------------- ###

    def get(self, key: str):
        print("get", key)
        print(self.db[key])

    def put(self, pair: str):
        print("PUT ", pair)
        self.db = self.db | json.loads(pair)
        self.write_db_to_file()

    def put_from_file(self, file_path: str, db: dict):
        self.db = db | self.read_file(file_path)
        self.write_db_to_file()

    def delete(self, key: str):
        print("delete ", key)
        self.db.pop(key)
        self.write_db_to_file()
