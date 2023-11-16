"""Order utils."""
from typing import Tuple, Union
from . import pizza_classes
from .Order import Order


def make_order(pizzas: Tuple[str], delivery: bool) -> None:
    """
    Bake and deliver pizzas.

    Args:
        pizzas (Tuple[str]): ordered pizzas.
        delivery (bool): need to delivery flag.
    """
    client_pizzas = [pizza_classes.__dict__[pizza.capitalize()]()
                     for pizza in pizzas]
    print('Order:', end='\n\t-')
    print('\n\t-'.join([str(pizza) for pizza in client_pizzas]))
    client_order = Order(*client_pizzas)
    client_order.bake()
    if delivery:
        client_order.delivery()
    else:
        client_order.pickup()


def print_showcase(items: Union[list[str], None] = None) -> None:
    """
    Print showcase items.

    If items is None than standart showcase items used:
        items = ['Margherita', 'Pepperoni', 'Hawaiian']
    Args:
        items (Union[List[str], None], optional): A list of pizza names.
                                                  Defaults to None.

    """
    if not items:
        items = ['Margherita', 'Pepperoni', 'Hawaiian']
    for pizza in items:
        pizza_instance = pizza_classes.__dict__[pizza]()
        pizza_ingridenets = ', '.join(sorted(list(
            pizza_instance.dict()[pizza]
            )))
        print(f'- {pizza}{pizza_instance.spec_symb}: {pizza_ingridenets}.')
