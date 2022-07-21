import os
import json


class Database:

    def __int__(self, location: str):
        self.db_location = location

    def write_db(self, data: dict):
        with open(self.db_location) as my_file:
            json.dump(data, my_file)

    def read_db(self, location=None) -> dict:
        if location is None:
            location = self.db_location

        with open(self.db_location) as my_file:
            data: dict = json.load(my_file)
        return data

    def put_from_file(self, file_path: str, db: dict):
        data = self.read_db(file_path)
        db = db | data
        self.write_db(db)

    def get(self, key: str, db: dict):
        print("get", key)
        print(db[key])

    def put(self, pair, db: dict):
        print("PUT ", pair)
        db = db | json.loads(pair)
        self.write_db(db)

    def delete(self, key: str, db: dict):
        print("delete ", key)
        db.pop(key, None)
        self.write_db(db)
