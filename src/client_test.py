from .base import Client


def client_context_test():
    with Client.Client(host='http://localhost', port=8080) as client:
        client.put('foo', 'bar')
        client.put("hello", "world")
        client.put("mnet", "media.net")
        client.show()
        client.delete('foo')
        client.show()
        client.truncate()
        client.show()


def client_test():
    # todo : take these args from config

    client = Client.Client(host='http://localhost', port=8080)

    client.put('foo', 'bar')
    client.put("hello", "world")
    client.put("mnet", "media.net")
    client.show()
    client.delete('foo')
    client.show()
    client.truncate()
    client.show()


def start():
    # client_test()
    client_context_test()
