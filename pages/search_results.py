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

    :param search_input: Locator for the search input
    :type search_input: Tuple[By.locator_strategy, locator]
    :param result_links: List of result links
    :type result_links: List[str]
    :param webdriver: selenium Webdriver object which can be used to
        interact with the web elements
    :type webdriver:
    """

    search_input = (By.NAME, 'q')
    result_links = (By.CSS_SELECTOR, "div[id='rso'] div[class='yuRUbf']")

    def __init__(self, webdriver) -> None:
        self.webdriver = webdriver

    def get_result_link_titles(self) -> list:
        """Collects the titles for all the results on the page.

        :return: List of titles
        :rtype: List[str]
        """
        links = self.webdriver.find_elements(*self.result_links)
        titles = [link.text for link in links]
        return titles

    def get_search_input_value(self) -> str:
        """Returns the search phrase used for the search.

        :return: The search basis
        :rtype: str
        """
        input_field = self.webdriver.find_element(*self.search_input)
        return input_field.get_attribute('value')

    @property
    def title(self) -> str:
        """Property to return the page title

        :return: Page title
        :rtype: str
        """
        return self.webdriver.title
