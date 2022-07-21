#!/bin/python3

import click


@click.command()
@click.option('--GET', default=1, help='Get the key from store')
def get_function(GET):
    print(GET)


@click.option('--put', default=1, help='Put the key in store.')
def put_function(put):
    print(put)


@click.option('--DEL', default=1, help='Delete the key from store')
def del_function(DEL):
    print(DEL)

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")


def start():
    hello()
    get_function()
    put_function()
    del_function()
