"""Enterpoint."""
import json
from src.advert_utils import Advert

if __name__ == '__main__':
    json_str = """{
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
    json_obj = json.loads(json_str)
    adv = Advert(json_obj)
    print(adv)
