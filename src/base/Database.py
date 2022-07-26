import json
import os.path


class Database:

    def __init__(self, name: str = "default.db"):
        """initialize DB location, creates an empty DB and loads it into memory"""

        self.__db_name = name

        if not os.path.isfile(self.__db_name):
            self._reset_db()
        else:
            with open(self.__db_name) as my_db:
                self._load_db(my_db)

    def _load_db(self, db_file):
        self.db: dict = json.load(db_file)

    def _reset_db(self) -> None:
        with open(self.__db_name, 'w+') as my_db:
            # some key and value are needed for json to read the file
            json.dump({"": ""}, my_db, indent=4)
            my_db.seek(0)
            self._load_db(my_db)

    def _write_db_to_file(self) -> None:
        """write json data to file"""

        # check lock, if its there then wait
        ### code
        # create lock
        with open(self.__db_name, 'w') as my_file:
            json.dump(self.db, my_file, indent=4)

            # If we don't seek to start, the json won't be able to read since after end, it's all empty
            my_file.seek(0, 0)
        # remove lock

    def _read_file(self, location) -> dict:
        """load json data from file"""
        with open(location) as my_file:
            data: dict = json.load(my_file)
        return data

    def set_db_name(self, name: str) -> str:
        self.__db_name = name
        return f"Successfully updated DB location to {self.__db_name}"

    def get_db_name(self) -> str:
        return self.__db_name

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
            self._write_db_to_file()
            return f"PUT:: Successfully put {key}={value} in Database"
        except:
            return f"PUT:: Some error occurred while putting {pair} in DB"

    # Todo : update this
    def put_from_file(self, file_path: str) -> str:
        """put values from json-fied file to DB"""

        self.db = self.db | self._read_file(file_path)
        self._write_db_to_file()
        return f"Successfully Added entries from {file_path} in DB"

    def delete(self, key: str) -> str:
        """delete the key from DB"""

        try:
            self.db.pop(key)
            self._write_db_to_file()
            return f"DELETE:: Successfully deleted {key} from DB"
        except KeyError:
            return f"DELETE:: Key {key} does not exist in DB"

    def show(self) -> dict:
        """returns the database as dict"""
        return self.db

    def truncate(self) -> str:
        """truncate current DB"""
        self._reset_db()
        return f"TRUNCATE:: Successfully truncated the DB"
