"""Test pizza classes."""
from src.pizza_classes import BasePizza, Margherita


def get_base_pizza_dict():
    """Return standart BasePizza fields dictionary."""
    pizza_dict = {
        'ingredients': {'tomate sauze', 'mozzarella'},
        'size': 'L',
        'spec_symb': '🧑‍🍳',
        '_pizza_type': 'BasePizza'
        }
    return pizza_dict


def test_topings():
    """Test add/delete toppings."""
    pizza = Margherita()
    margherita_ingredients = pizza.ingredients.copy()
    pizza.add_topings('chocolate')
    assert pizza.ingredients == margherita_ingredients.union({'chocolate'})
    assert 'chocolate' in str(pizza)
    pizza.delete_toppings('chocolate', 'tomatoes')
    assert pizza.ingredients == margherita_ingredients.difference({'tomatoes'})


def test_equal():
    """Test __eq__ for pizzas classes."""
    margherita = Margherita()
    base_pizza = BasePizza()
    pizza_dict = get_base_pizza_dict()
    assert margherita == Margherita()
    assert not (base_pizza != BasePizza())
    assert margherita != base_pizza
    assert BasePizza != pizza_dict
    base_pizza.add_topings('tomatoes')
    assert base_pizza == margherita
    margherita.delete_toppings('tomatoes')
    assert base_pizza != margherita


def test_dict():
    """Test dict method for BasePizza class."""
    ingredients = get_base_pizza_dict()['ingredients']
    pizza_ingr_dict = {'BasePizza': ingredients}
    assert pizza_ingr_dict == BasePizza().dict()
