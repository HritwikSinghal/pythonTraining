import requests

from requests.exceptions import ConnectionError


class Client:
    """Class for creating a client program"""

    def __init__(self, host: str, port: int, db_name: str = "client.db", api_version: int = 1):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.api_version = api_version

        self.url = f"{self.host}:{self.port}/api/v{self.api_version}"

        # self.check_connection_to_server()

    def __enter__(self):
        my_client = Client(self.host, self.port, db_name=self.db_name, api_version=1)
        my_client.create()
        return my_client

    def __exit__(self, exc_type, exc_value, exc_traceback) -> str:
        return "Client Exiting..."

    # Todo: fix this
    def check_connection(self) -> bool:
        """checks connection if server is reachable"""
        try:
            if requests.get(self.url).ok:
                return True
        except ConnectionError or Exception as e:
            # print(e)
            # raise Exception("Check if server is running properly")
            return False

    def create(self) -> bool:
        """create a new DB with specified name"""
        return requests.post(self.url + '/create', params={'db_name': self.db_name}).__bool__()

    def help(self):
        """Show help page from server"""
        print(requests.get(self.url + "/help").json())

    def show(self):
        """list the entire contents of the remote DB """
        print(requests.get(self.url + "/show").json())

    def get(self, key: str):
        """Get the value of key from DB"""
        params: dict = {"key": key}
        print(requests.get(self.url, params=params))

    def put(self, key: str, value: str):
        """calls the server and returns the value of `key`"""
        params: dict = {"key": key, "value": value}
        print(requests.put(url=self.url, params=params).json())

    def delete(self, key: str):
        """Delete key from database"""
        params: dict = {"key": key}
        print(requests.delete(self.url, params=params).json())

    def truncate(self, i_am_sure: bool = False):
        params = {"i_am_sure": i_am_sure}
        print(requests.post(self.url + "/truncate", params=params).json())
