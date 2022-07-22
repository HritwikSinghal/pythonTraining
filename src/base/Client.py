import requests


class Client():
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.url = f"{self.host}:{self.port}"

    def __get_content(self, url: str, params=None) -> dict:
        if params is None:
            params = {}

        x = requests.get(url, params=params)
        return x.json()
        # if x.status_code == 200:
        #     return x.json()
        # else:
        #     return f"GET ERROR: HTTP Code={x.status_code}, url={x.url}"

    def __put_content(self, url, params=None) -> dict:
        if params is None:
            params = {}

        x = requests.put(url=url, params=params)
        return x.json()

    ### ---------------------------------------------------------- ###

    def help(self):
        """Show help page from server"""
        return self.__get_content(self.url + "/help")

    def show(self):
        """list the entire contents of the remote kvstore """
        return self.__get_content(self.url + "/show")

    def get(self, key: str):
        """Get the value of key from DB"""
        params = {"key": key}
        return self.__get_content(self.url, params=params)

    def put(self, key: str, value: str):
        """calls the server and returns the value of `key`"""
        params = {"key": key, "value": value}
        return self.__put_content(self.url, params=params)

    def delete(self, key: str) -> int:
        """Delete key from database"""
        params = {"key": key}
        return requests.delete(self.url, params=params).status_code
