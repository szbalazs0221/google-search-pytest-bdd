"""This module contains a ``GoogleSearchPage`` class. Instances of this
class can be used in tests to interact with the ``GoogleSearchPage`` page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage:
    """Class for creating GoogleSearchPage object.
    """

    url = 'https://google.com'

    search_input = (By.NAME, 'q')
    consent_iframe = (By.CSS_SELECTOR, 'div[id=cnsw] iframe')
    agree = (By.CSS_SELECTOR, "div[id=introAgreeButton]")

    def __init__(self, browser) -> None:
        self.browser = browser

    def load(self):
        """Loads the search page.
        """
        self.browser.get(self.url)

    def agree_to_cookies(self) -> None:
        """Agrees to all cookies to be able to start using the search page.
        """
        frame = self.browser.find_element(*self.consent_iframe)
        self.browser.switch_to.frame(frame)
        button = self.browser.find_element(*self.agree)
        button.click()

    def search(self, phrase) -> None:
        """Initiate a search on the search page with the given phrase.

        :param phrase: Search phrase
        :type phrase: str
        """
        search_input = self.browser.find_element(*self.search_input)
        search_input.send_keys(phrase + Keys.RETURN)
