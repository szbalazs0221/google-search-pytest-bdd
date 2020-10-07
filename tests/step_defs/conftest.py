"""Fixtures for steps definitions."""
import pytest
import selenium.webdriver

CHROME = 'Chrome'
FIREFOX = 'Firefox'
IE = 'IE'
SAFARI= 'Safari'


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

CHROME = 'Chrome'
FIREFOX = 'Firefox'
IE = 'IE'
SAFARI= 'Safari'


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
