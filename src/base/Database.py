import json
import os.path


class Database:

    def __init__(self):
        self.db_location = "my_db.db"
        if not os.path.isfile(self.db_location):
            with open(self.db_location, 'w+') as my_db:
                # some key and value are needed for json to read the file
                json.dump({"": ""}, my_db, indent=4)
                my_db.seek(0)
                self.db: dict = json.load(my_db)
        else:
            with open(self.db_location) as my_db:
                self.db: dict = json.load(my_db)

    def __int__(self, location: str):
        self.db_location = location
        with open(self.db_location) as my_db:
            self.db: dict = json.load(my_db)

    def write_db_to_file(self) -> None:
        # Very Poorly optimized
        with open(self.db_location, 'w') as my_file:
            json.dump(self.db, my_file, indent=4)

            # If we don't seek to start, the json won't be able to read since after end, it's all empty
            my_file.seek(0, 0)

    def read_file(self, location) -> dict:
        with open(location) as my_file:
            data: dict = json.load(my_file)
        return data

    ### --------------------------------------------------------------------- ###

    def get(self, key: str) -> str:
        # print("get", key)
        # print(json.dumps(self.db, indent=3))
        try:
            return f'{key}={self.db[key]}'
        except KeyError:
            return f"Key {key} does not exist in DB"

    def put(self, pair: str) -> str:
        # print("PUT ", pair)
        key, value = pair.split("=")
        self.db = self.db | json.loads(f'{{"{key}": "{value}"}}')
        self.write_db_to_file()
        return f"Successfully put {key}={value} in Database"

    def put_from_file(self, file_path: str) -> None:
        self.db = self.db | self.read_file(file_path)
        self.write_db_to_file()

    def delete(self, key: str) -> None:
        # print("delete ", key)
        try:
            self.db.pop(key)
        except KeyError:
            print("Key does not exist in DB")
        self.write_db_to_file()

    def show_db(self) -> dict:
        return self.db
