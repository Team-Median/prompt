from prompt.flight_club_scraper import fc_site_search
from prompt import __version__
import pytest

def test_item_not_available():
    search_string = ""
    result = 0
    fc_site_search('http://www.flightclub.com/', search_string)
    if result == 0:
        return "Still out of stock"
    else:
        result > 1
        return ''
        actual = result
        expected = 1
        assert actual == expected


def test_version():
    assert __version__ == '0.1.0'
