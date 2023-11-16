"""Pizza classes."""
from .log_utils import log


class BasePizza:
    """Base pizza, consisting only mozzarella and tomate sauze."""

    def __init__(self, size='XL'):
        """
        Initialize a pizza size, base ingredients, spec_symb.

        Args:
            size (str, optional): Pizza size (ex. L, XL). Defaults to 'XL'.
        """
        self.size = size
        self.ingredients = {'tomate sauze', 'mozzarella'}
        self.spec_symb = '🧑‍🍳'
        self._pizza_type = self.__class__.__name__

    def __str__(self) -> str:
        """
        Return a string descreption of pizza.

        In format:
            {class_name} size {size} with ingredients: {a}, {b}, {c}.
        Return:
            str: descreption of a pizza.
        """
        res = f'{self._pizza_type}{self.spec_symb} size {self.size} with '
        res += f'ingredients: {", ".join(sorted(list(self.ingredients)))}.'
        return res

    def __eq__(self, __value: object) -> bool:
        """
        Compare the self pizza with __value.

        Args:
            __value (object): object to compare.

        Returns:
            bool: True if the pizzas are equal, False otherwise.
        """
        if not isinstance(__value, BasePizza):
            return False

        if self.size == __value.size and \
           self.ingredients == __value.ingredients:
            return True
        return False

    def add_topings(self, *topings: str) -> None:
        """
        Add toppings to the pizza.

        Args:
            *toppings (str): toppings to add.
        """
        self.ingredients = self.ingredients.union(set(topings))

    def delete_toppings(self, *topings: str) -> None:
        """
        Delete toppings from the pizza.

        Args:
            *toppings (str): toppings to delete.
        """
        for t in topings:
            self.ingredients.remove(t)

    @log()
    def bake(self, log_baking=True) -> None:
        """
        Bake one pizza.

        Args:
            pizza (BasePizza): pizza to bake.
        """
        if log_baking:
            print(f'Baking {self._pizza_type}:', end='\n\t')

    def dict(self) -> dict:
        """
        Return a dictionary representing the pizza.

        Returns:
            dict:   A dictionary with the pizza type as the key
                    and its ingredients as the value.
        """
        return {self._pizza_type: self.ingredients}


class Margherita(BasePizza):
    """Class for margherita pizza."""

    def __init__(self, size='XL'):
        """Init a pizza size, ingredients, spec_symb."""
        super().__init__(size)
        self.add_topings('tomatoes')
        self.spec_symb = '🧀'


class Pepperoni(BasePizza):
    """Class for pepperoni pizza."""

    def __init__(self, size='XL'):
        """Init a pizza size, ingredients, spec_symb."""
        super().__init__(size)
        self.add_topings('pepperoni')
        self.spec_symb = '🍕'


class Hawaiian(BasePizza):
    """Class for hawaiian pizza."""

    def __init__(self, size='XL'):
        """Init a pizza size, ingredients, spec_symb."""
        super().__init__(size)
        self.add_topings('chicken', 'pineapples')
        self.spec_symb = '🍍'
