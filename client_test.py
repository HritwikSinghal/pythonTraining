from src.base import Client


def client_context_test():
    with Client.Client(host='http://localhost', port=8080, db_name='client_context_test.db', api_version=1) as client:
        client.put('foo', 'bar')
        client.put("hello", "world")
        client.put("mnet", "media.net")
        client.show()
        client.delete('foo')
        client.show()
        client.truncate(i_am_sure=True)
        client.show()


def client_test():
    # todo : take these args from config

    client = Client.Client(host='http://localhost', port=8080, db_name="client_test.db", api_version=1)

    if client.create():
        client.put('foo', 'bar')
        client.put("hello", "world")
        client.put("mnet", "media.net")
        client.show()
        client.delete('foo')
        client.show()
        client.truncate(i_am_sure=False)
        client.show()


def start():
    # client_context_test()
    client_test()
