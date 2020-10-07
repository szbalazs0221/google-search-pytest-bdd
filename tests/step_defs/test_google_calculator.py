"""This module contains step definitions for testing google search
calculator capabilities"""

from pytest_bdd import scenarios, parsers, given, when, then
from pages.search_page import GoogleSearchPage
from pages.search_results import GoogleSearchResults

# actually it is not mandatory, because default type is string
CONVERTERS = {'mathmematical_phrase': str, 'result': str}

scenarios('../features/google_search_calculator.feature',
          example_converters=CONVERTERS)


@when(parsers.parse(
    'the user types "<mathmematical_phrase>" in the search page')
)
def mathematical_phrase(search_page, mathmematical_phrase):
    search_page.search(mathmematical_phrase)


@then(parsers.parse('Google should return "<result>"'))
def math_result(webdriver, result):
    cal_display = GoogleSearchResults(webdriver)
    assert cal_display.show_calculator_display() == result
