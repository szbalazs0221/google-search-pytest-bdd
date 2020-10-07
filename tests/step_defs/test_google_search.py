"""This module contains step definitions for google_search.feature file"""

from pytest_bdd import scenario, given, when, then 

from pages.search_page import GoogleSearchPage
from pages.search_results import GoogleSearchResults


def test_search(webdriver):
    page = GoogleSearchPage(webdriver)
    page.load()
    page.agree_to_cookies()
    page.search('Panda')
    result = GoogleSearchResults(webdriver)
    titles = result.get_result_link_titles()
    assert 'panda' in titles[0]
