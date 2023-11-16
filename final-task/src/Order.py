"""Utils for make a order."""
from .pizza_classes import BasePizza
from .log_utils import log


class Order:
    """Order class."""

    def __init__(self, *pizzas: BasePizza) -> None:
        """Init order items and status."""
        self._pizzas = pizzas
        self.status = 'not baked'

    def bake(self) -> 'Order':
        """Bake all pizzas in order."""
        if self.status != 'not baked':
            return self
        logging_separately = True if len(self._pizzas) > 1 else False
        for pizza in self._pizzas:
            pizza.bake(logging_separately)
        self.status = 'baked'
        return self

    @log('🛵 Доставили за {}s!')
    def delivery(self) -> 'Order':
        """Delivery order."""
        if self.status == 'baked' and self.status != 'picked up':
            self.status = 'delivered'
        return self

    @log('🏠 Забрали за {}s!')
    def pickup(self) -> 'Order':
        """Order pick up."""
        if self.status == 'baked' and self.status != 'delivered':
            self.status = 'picked up'
        return self
