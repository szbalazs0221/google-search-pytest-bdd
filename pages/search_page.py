"""This module contains a :class:`GoogleSearchPage` class. Instances of this
class can be used in tests to interact with the search page.

Example:
========
>>> import selenium.webdriver
>>> b = selenium.webdriver.Chrome()
>>> b.implicitly_wait(10)
>>> page = GoogleSearchPage(b)
>>> page.load()
>>> page.agree_to_cookies()
>>> page.search('car')
"""

from typing import Any

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

Webdriver = Any


class GoogleSearchPage:
    """Class for creating a GoogleSearchPage object. This is a blueprint of
    the search page where different searches can be initiated.

    :param url: Url for Google search
    :type url: str
    :param search_input: Locator for the search input
    :type search_input: Tuple[By.locator_strategy, locator]
    :param consent_iframe: Locator for the consent pop-up page
    :type consent_iframe: Tuple[By.locator_strategy, locator]
    :param agree_button: Button to accept all cookies
    :type agree_button: Tuple[By.locator_strategy, locator]
    """

    url = 'https://google.com'

    search_input = (By.NAME, 'q')
    consent_iframe = (By.CSS_SELECTOR, 'div[id=cnsw] iframe')
    agree_button = (By.CSS_SELECTOR, "div[id=introAgreeButton]")

    def __init__(self, browser: Webdriver) -> None:
        self.browser = browser

    def load(self) -> None:
        """Loads the search page.
        """
        self.browser.get(self.url)

    def agree_to_cookies(self) -> None:
        """Agrees to all cookies to be able to start using the search page.
        """
        frame = self.browser.find_element(*self.consent_iframe)
        self.browser.switch_to.frame(frame)
        button = self.browser.find_element(*self.agree_button)
        button.click()

    def search(self, phrase: str) -> None:
        """Initiate a search on the search page with the given phrase.

        :param phrase: Search phrase
        :type phrase: str
        """
        search_input = self.browser.find_element(*self.search_input)
        search_input.send_keys(phrase + Keys.RETURN)
