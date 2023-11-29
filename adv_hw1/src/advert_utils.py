"""Advert class."""
from keyword import iskeyword
from typing import Union
Number = Union[int, float]


class AdvertNestedKey():
    """Class for using dict nested keys as attributes."""

    def __init__(self, mapping: dict):
        """
        Init nested dict.

        Args:
            mapping (Dict): dict for which we want get values from attributes
        """
        for key in mapping:
            if isinstance(mapping[key], dict):
                self.__dict__[key] = AdvertNestedKey(mapping[key])
            else:
                self.__dict__[key] = mapping[key]

    def __getattr__(self, key: str):
        """Return the attribute for getted key (str)."""
        print(self.__dict__)
        if key[-1] == '_' and iskeyword(key[:-1]):
            key = key[:-1]
        return self.__dict__[key]

    def __str__(self, lvl=0) -> str:
        """Convert self to str format. lvl is identation level."""
        # Сделел так, потому что из примера неясно,
        # как должны отображаться вложенные дикты
        strt = '_' * lvl * 5
        res = []
        nesteds = []
        for key in self.__dict__:
            if not isinstance(self.__dict__[key], AdvertNestedKey):
                res.append(strt + str(self.__dict__[key]))
            else:
                nesteds.append(key)
        for key in nesteds:
            res.append(strt + '| ' + key + ':')
            res.append(
                self.__dict__[key].__str__(lvl+1)
                )
        return '\n'.join(res)


class ColorMixin:
    """Mixin for change __str__ color."""

    # Добавлять color_code в Advert мне показалось странной идеей.
    # Потому что, если бы убираем миксин, то к чему этот color_code тогда?
    # Так что я сделал так. Без миксина никаких настроек цвета.
    color_code = 32

    def __str__(self, color=None) -> str:
        """Redefine __str__ with changed color."""
        if color is None:
            color = ColorMixin.color_code
        res = f'\033[1;{color};40m' + super().__str__()
        res += '\033[0;37;40m'
        return res


class Advert(ColorMixin, AdvertNestedKey):
    """Advert class."""

    def __init__(self, mapping: dict) -> None:
        """Init Advert."""
        self.check_title(mapping)
        self._price: Number = 0
        if 'price' in mapping:
            self.price = mapping['price']
            mapping.pop('price')
        super().__init__(mapping)

    @staticmethod
    def check_title(mapping) -> None:
        """
        Check that title in mapping and title is string.

        If someting worng, raises ValueError.
        """
        if 'title' not in mapping:
            raise ValueError('title must be in mapping.')
        if not isinstance(mapping['title'], str):
            raise ValueError('title must be a string.')

    @property
    def price(self) -> Number:
        """Price getter."""
        return self._price

    @price.setter
    def price(self, value: Number) -> None:
        """Price setter."""
        if not isinstance(value, (float, int)):
            raise ValueError("Price must be a number")
        if value < 0:
            raise ValueError("Price must be not negative number.")
        self._price = value
