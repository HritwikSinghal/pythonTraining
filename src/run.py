import click

from src import GET, PUT, DEL


@click.command()
@click.option('--get', help='Get the key from store', type=str)
@click.option('--put', help='Put the key in store.', type=str)
@click.option('--delete', help='Delete the key from store', type=str)
@click.option('--count', default=1, help='Number of greetings.', type=int)
@click.option('--name', default="Hritwik", help='The person to greet.', type=str)
def start(get, put, delete, count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

    GET.get_function(get)
    PUT.put_function(put)
    DEL.del_function(delete)
