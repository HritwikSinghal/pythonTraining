import requests


class Client:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.url = f"{self.host}:{self.port}"

    def __enter__(self):
        self._client = Client(self.host, self.port)
        return self._client

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

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
