"""This module contains step definitions for google_search.feature file"""
from pytest_bdd import scenario, then, when
from pages.search_results import GoogleSearchResults


@scenario('../features/google_search.feature', 'Simple search')
def test_search():
    """Search test scenario.
    """


@when('the user search for the phrase car')
def search_phrase(search_page):
    """Step definition for searching Car.

    :param search_page: Search page in a state for ready to search
    :type search_page: :class:`GoogleSearchPage`
    """
    search_page.search('Car')


@then('the results are shown for car')
def search_results(webdriver):
    """Step definition for getting back the link titles from the Search
    results, than assert if 'car' is in the titles.

    :param webdriver: webdriver fixture
    :type webdriver: selenium.webdriver
    """
    results = GoogleSearchResults(webdriver)
    titles = results.get_result_link_titles()
    assert 'car' in titles[0].lower()
