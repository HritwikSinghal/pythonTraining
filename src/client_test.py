from .base import Client


# Todo: implement this
def client_context_test():
    with Client.Client(..., port=8080) as client:
        client.put('foo', 'bar')


def start():
    # todo : take these args from config
    client = Client.Client(host='http://localhost', port=8080)

    # client.put('foo', 'bar')
    # client.put("hello", "world")
    # client.put("mnet", "media.net")
    # client.delete('baz')
    client.show()
