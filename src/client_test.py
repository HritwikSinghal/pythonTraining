from .base import Client


# Todo: implement this
def client_context_test():
    with Client.Client(..., port=8080) as client:
        client.put('foo', 'bar')


def start():
    # todo : take these args from config
    client = Client.Client(host='http://localhost', port=8080)

    print(client.put('foo', 'bar'))
    print(client.put("hello", "world"))
    print(client.put("mnet", "media.net"))
    # print(client.delete('baz'))
    print(client.show())
