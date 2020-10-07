"""Fixtures for steps definitions."""
import pytest
import selenium.webdriver

from pytest_bdd import given
from pages.search_page import GoogleSearchPage

CHROME = 'Chrome'
FIREFOX = 'Firefox'
IE = 'IE'
SAFARI = 'Safari'


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

    if driver == CHROME:
        browser = selenium.webdriver.Chrome()
    elif driver == FIREFOX:
        browser = selenium.webdriver.Firefox()
    elif driver == IE:
        browser = selenium.webdriver.Ie()
    elif driver == SAFARI:
        browser = selenium.webdriver.Safari()

    browser.implicitly_wait(10)
    yield browser
    browser.quit()


def pytest_addoption(parser):
    """Custom command line options.

    :param parser: Parser for command line arguments and ini-file values.
    :type parser: Parser
    """
    parser.addoption(
        "--webdriver",
        action='store',
        choices=[CHROME, FIREFOX, IE, SAFARI],
        required=True)


@given('the Google Search page is displayed', target_fixture="search_page")
def display_search_page(webdriver):
    page = GoogleSearchPage(webdriver)
    page.load()
    page.agree_to_cookies()
    page.switch_to_english()
    return page


def pytest_bdd_step_error(step_func_args):
    step_func_args['webdriver'].save_screenshot("screenshot.png")
