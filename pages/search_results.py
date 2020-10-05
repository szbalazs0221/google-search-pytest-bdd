"""This module contains a ``GoogleSearchResult`` class. Instances of this
class can be used in tests to interact with the ``GoogleSearchResult`` Page.
"""

from selenium.webdriver.common.by import By


class GoogleSearchResults:
    """Class for creating GoogleSearchResult object.
    """

    search_input = (By.NAME, 'q')
    result_links = (By.CSS_SELECTOR, "div[id='rso'] div[class='yuRUbf']")

    def __init__(self, browser) -> None:
        self.browser = browser

    def get_result_link_titles(self) -> tuple:
        links = self.browser.find_elements(*self.result_links)
        titles = [link.text for link in links]
        return titles
