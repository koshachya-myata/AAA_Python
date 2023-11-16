"""Pizza Ordering System command-line interface."""
import click
from src.interaction_utils import make_order, print_showcase
from typing import Tuple


@click.group()
def cli():
    """Pizza Ordering System."""
    pass


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizzas", nargs=-1)
def order(pizzas: Tuple[str], delivery: bool):
    """
    Bake and deliver pizzas.

    Uses click CLI.
    Args:
        pizzas (Tuple[str]): ordered pizzas.
        delivery (bool): need to deliver flag.
    """
    make_order(pizzas, delivery)


@cli.command()
def menu():
    """Print menu."""
    print_showcase()


if __name__ == '__main__':
    cli()
