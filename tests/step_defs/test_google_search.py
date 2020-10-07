"""This module contains step definitions for google_search.feature file"""

from pytest_bdd import scenario, given, when, then

from pages.search_page import GoogleSearchPage
from pages.search_results import GoogleSearchResults


@scenario('../features/google_search.feature', 'Simple search')
def test_search():
    pass

@given('the Google Search page is displayed', target_fixture="search_page")
def display_search_page(webdriver):
    page = GoogleSearchPage(webdriver)
    page.load()
    page.agree_to_cookies()
    page.switch_to_english()
    return page

@when('the user search for the phrase car')
def search_phrase(search_page):
    search_page.search('Car')

@then('the results are shown for car')
def search_results(webdriver):
    results = GoogleSearchResults(webdriver)
    titles = results.get_result_link_titles()
    assert 'car' in titles[0].lower()
