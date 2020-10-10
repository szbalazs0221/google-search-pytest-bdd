"""Test level fixtures and common step definitions"""
import pytest
import selenium.webdriver

from pytest_bdd import given
from pages.search_page import GoogleSearchPage


@pytest.fixture()
def webdriver(request):
    """Webdriver fixture used for tests. This will setup a webdriver
    based on command line input, pass it over to a test, then quit the
    webdriver after the test is completed.

    :param request: The request fixture is a special fixture providing
        information of the requesting test function.
    :type request: fixture
    :yield: Active webdriver
    :rtype: selenium.webdriver
    """
    driver = request.config.getoption("--webdriver")

    if driver == 'Chrome':
        browser = selenium.webdriver.Chrome()
    elif driver == 'Firefox':
        browser = selenium.webdriver.Firefox()
    elif driver == 'Ie':
        browser = selenium.webdriver.Ie()
    elif driver == 'Edge':
        browser = selenium.webdriver.Edge()

    browser.implicitly_wait(10)
    yield browser
    browser.quit()

# common step definitions


@given('the Google Search page is displayed', target_fixture="search_page")
def display_search_page(webdriver):
    page = GoogleSearchPage(webdriver)
    page.load()
    page.agree_to_cookies()
    page.switch_to_english()
    return page
