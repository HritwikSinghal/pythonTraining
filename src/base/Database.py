import json
import os.path


class Database:

    def __init__(self):
        """default constructor, creates an empty DB and loads it into memory"""
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
        """initialize DB location and import DB"""

        self.db_location = location
        with open(self.db_location) as my_db:
            self.db: dict = json.load(my_db)

    def write_db_to_file(self) -> None:
        """write json data to file"""
        # Very Poorly optimized
        with open(self.db_location, 'w') as my_file:
            json.dump(self.db, my_file, indent=4)

            # If we don't seek to start, the json won't be able to read since after end, it's all empty
            my_file.seek(0, 0)

    def read_file(self, location) -> dict:
        """load json data from file"""
        with open(location) as my_file:
            data: dict = json.load(my_file)
        return data

    ### --------------------------------------------------------------------- ###

    def get(self, key: str) -> str:
        """get value of key from DB"""
        try:
            return f'GET:: {key}={self.db[key]}'
        except KeyError:
            return f"GET:: Key {key} does not exist in DB"

    def put(self, pair: str) -> str:
        """Put key, value in DB"""
        try:
            key, value = pair.split("=")
            self.db = self.db | json.loads(f'{{"{key}": "{value}"}}')
            self.write_db_to_file()
            return f"PUT:: Successfully put {key}={value} in Database"
        except:
            return f"PUT:: Some error occurred while putting {pair} in DB"

    # Todo : update this
    def put_from_file(self, file_path: str) -> str:
        """put values from json-fied file to DB"""

        self.db = self.db | self.read_file(file_path)
        self.write_db_to_file()
        return f"Successfully Added entries from {file_path} in DB"

    def delete(self, key: str) -> str:
        """delete the key from DB"""

        try:
            self.db.pop(key)
            self.write_db_to_file()
            return f"DELETE:: Successfully deleted {key} from DB"
        except KeyError:
            return f"DELETE:: Key {key} does not exist in DB"

    def show(self) -> dict:
        """returns the database as dict"""
        return self.db
