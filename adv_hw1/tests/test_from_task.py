"""Tests examples from task."""
import json
from src.advert_utils import Advert
import pytest

lesson_str = """{
        "title": "python",
        "class": "lang",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"],
            "nested": {
                "four": "two"
                }
            }
        }"""
lesson = json.loads(lesson_str)
lesson_ad = Advert(lesson)


def test_attrs():
    """Test dynamic attributes creation."""
    assert lesson_ad.location.address == 'город Москва, Лесная, 7'
    assert lesson_ad.title == 'python'
    assert lesson_ad.location.nested.four == 'two'
    assert lesson_ad.class_ == 'lang'


def test_price():
    """Test price functionality."""
    assert lesson_ad.price == 0
    assert Advert({"title": "qwe"}).price == 0
    with pytest.raises(ValueError):
        Advert({'title': 'bad_price', 'price': 'two hundred'})
    with pytest.raises(ValueError):
        Advert({'title': 'bad_price', 'price': -100})
    with pytest.raises(ValueError):
        lesson_ad.price = -15
    lesson_ad.price = 15
    assert lesson_ad.price == 15


def test_title():
    """Check that error raised if title not passed."""
    with pytest.raises(ValueError):
        Advert({"name": "Bob"})
