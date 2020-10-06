"""This module contains a class:`search_result.GoogleSearchResult` class.
Instances of this class can be used in tests to interact with the results page.

Example
=======
>>> import selenium.webdriver
>>> # Assuming you searched for some phrase with GoogleSearchPage.search()
>>> b = selenium.webdriver.Chrome()
>>> b.implicitly_wait(10)
>>> page = GoogleResultsPage(b)
>>> page.title
'{phrase} - Google search'
>>> page.get_search_input_value()
'Your search phrase'
>>> page.get_result_link_titles()
['result_link_1', 'result_link_2', ...]
"""

from selenium.webdriver.common.by import By


class GoogleSearchResults:
    """Class for creating a GoogleSearchResult object.

    :param search_input: 
    :type search_input:
    :param result_links:
    :type result_links:
    :param browser:
    :type browser:
    """

    search_input = (By.NAME, 'q')
    result_links = (By.CSS_SELECTOR, "div[id='rso'] div[class='yuRUbf']")

    def __init__(self, browser) -> None:
        self.browser = browser

    def get_result_link_titles(self) -> list:
        links = self.browser.find_elements(*self.result_links)
        titles = [link.text for link in links]
        return titles

    def get_search_input_value(self) -> str:
        input_field = self.browser.find_element(*self.search_input)
        return input_field.get_attribute('value')

    @property
    def title(self) -> str:
        return self.browser.title
