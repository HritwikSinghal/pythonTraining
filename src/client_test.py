from .base import Client


# Todo: implement this
def client_context_test():
    with Client.Client(..., port=8080) as client:
        client.put('foo', 'bar')


def client_test():
    # todo : take these args from config
    client = Client.Client(host='http://localhost', port=8080)

    # print(client.help())
    # print(client.show())
    # client.put('foo', 'bar')
    client.put('baz', 'foobar')
    print(client.get('baz'))
    print(client.show())

    stat_code = client.delete('baz')
    if stat_code == 200:
        print(f"Key successfully deleted")

    print(client.show())
