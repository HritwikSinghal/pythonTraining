import requests


class Client:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.url = f"{self.host}:{self.port}"

    def help(self):
        """Show help page from server"""
        return requests.get(self.url + "/help").json()

    def show(self):
        """list the entire contents of the remote kvstore """
        return requests.get(self.url + "/show").json()

    def get(self, key: str):
        """Get the value of key from DB"""
        params = {"key": key}
        return requests.get(self.url, params=params)

    def put(self, key: str, value: str):
        """calls the server and returns the value of `key`"""
        params = {"key": key, "value": value}
        x = requests.put(url=self.url, params=params)
        return x.json()

    def delete(self, key: str) -> int:
        """Delete key from database"""
        params = {"key": key}
        return requests.delete(self.url, params=params).status_code
