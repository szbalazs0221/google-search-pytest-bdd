"""This module contains step definitions for testing google search
calculator capabilities"""

from pytest_bdd import scenarios, parsers, when, then
from pages.search_results import GoogleSearchResults

# actually this is not mandatory, because default type is string
CONVERTERS = {'mathmematical_phrase': str, 'result': str}

scenarios('../features/google_search_calculator.feature',
          example_converters=CONVERTERS)


@when(parsers.parse(
    'the user types "<mathmematical_phrase>" in the search page')
)
def mathematical_phrase(search_page, mathmematical_phrase):
    """Step definition for passing a mathematical phrase into the search field.

    :param search_page: Search page in a state for ready to search
    :type search_page: :class:`GoogleSearchPage`
    :param mathmematical_phrase: Simple mathematical phrase, e.g.: **"5 + 5"**
    :type mathmematical_phrase: str
    """
    search_page.search(mathmematical_phrase)


@then(parsers.parse('Google should return "<result>"'))
def math_result(webdriver, result):
    """Step definition for getting back the result from the calculator and than
    assert the value with our expectation.

    :param webdriver: webdriver fixture
    :type webdriver: selenium.webdriver
    :param result: The expected result
    :type result: str
    """
    cal_display = GoogleSearchResults(webdriver)
    assert cal_display.show_calculator_display() == result
