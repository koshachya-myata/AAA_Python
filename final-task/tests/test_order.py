"""Tests order functionality."""
import pytest
from unittest.mock import patch
from src.interaction_utils import make_order
from src.pizza_classes import Hawaiian
from src.Order import Order


@patch('random.randint')
def test_make_order_print(randint):
    """Test make_order std-out output using 2 different cases."""
    output = ""

    def custom_print(*args, **kwargs):
        nonlocal output
        end = kwargs['end'] if 'end' in kwargs else '\n'
        output += ' '.join(map(str, args)) + end

    randint.return_value = 3
    with pytest.MonkeyPatch.context() as monkey_patch:
        monkey_patch.setattr('builtins.print', custom_print)
        make_order(('Margherita', 'pePPeroni', 'Hawaiian'), True)
    except_strings = [
        'Order:',
        '\t-Margherita🧀 size XL with ingredients: '
        'mozzarella, tomate sauze, tomatoes.',
        '\t-Pepperoni🍕 size XL with ingredients: '
        'mozzarella, pepperoni, tomate sauze.',
        '\t-Hawaiian🍍 size XL with ingredients: '
        'chicken, mozzarella, pineapples, tomate sauze.',
        'Baking Margherita:',
        '\tbake — 3s!',
        'Baking Pepperoni:',
        '\tbake — 3s!',
        'Baking Hawaiian:',
        '\tbake — 3s!',
        '🛵 Доставили за 3s!'
    ]
    excepted_print = '\n'.join(except_strings) + '\n'
    assert output == excepted_print

    output = ""
    with pytest.MonkeyPatch.context() as monkey_patch:
        monkey_patch.setattr('builtins.print', custom_print)
        make_order(('margherita', 'HAWAIIAN'), False)
    remove_indices = {2, 5, 6}
    except_strings = [val for ind, val in enumerate(except_strings)
                      if ind not in remove_indices]
    except_strings[-1] = '🏠 Забрали за 3s!'
    excepted_print = '\n'.join(except_strings) + '\n'
    assert output == excepted_print


def test_make_order_incorrect_pizza():
    """Test that incorrect pizza name in order raises error."""
    with pytest.raises(KeyError):
        make_order(('random_pizza'), True)
    with pytest.raises(KeyError):
        make_order(('Hawaiian', 'random_pizza'), False)


def test_order_statuses():
    """Test that order status changes correctly."""
    order = Order(Hawaiian(), Hawaiian())
    assert order.status == 'not baked'
    order.bake()
    assert order.status == 'baked'
    order.delivery()
    assert order.status == 'delivered'
    assert Order(Hawaiian()).bake().pickup().status == 'picked up'
