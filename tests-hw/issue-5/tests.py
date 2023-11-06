"""Tests for what_is_year_now."""
import pytest
from unittest.mock import patch
import urllib.request
from what_is_year_now import what_is_year_now, API_URL


def test_api_url():
    """Test that api url is correct."""
    try:
        urllib.request.urlopen(API_URL)
    except ValueError:
        pytest.fail('API url dosent work')


class UrlopenMock(object):
    """Class for mock urlopen."""

    def __init__(self) -> None:
        """Pass."""
        pass

    def __enter__(self):
        """Return self."""
        return self

    def __exit__(self, *args):
        """Pass."""
        pass


@patch('what_is_year_now.json.load')
@patch('what_is_year_now.urllib.request.urlopen')
def test_formats(urlopen, json_load):
    """Test different currentDateTime formats."""
    urlopen.return_value = UrlopenMock()
    json_load.return_value = {'currentDateTime': '2020-03-01'}

    assert what_is_year_now() == 2020
    json_load.return_value = {'currentDateTime': '01.03.2021'}
    assert what_is_year_now() == 2021


@patch('what_is_year_now.json.load')
@patch('what_is_year_now.urllib.request.urlopen')
def test_error_raised(urlopen, json_load):
    """Test that ValueError raised if incorrect data format."""
    urlopen.return_value = UrlopenMock()
    json_load.return_value = {'currentDateTime': '2020 03 01'}
    with pytest.raises(ValueError):
        what_is_year_now()
