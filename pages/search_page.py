"""This module contains a :class:`GoogleSearchPage` class. Instances of this
class can be used in tests to interact with the search page.

Example
=======
>>> import selenium.webdriver
>>> b = selenium.webdriver.Chrome()
>>> b.implicitly_wait(10)
>>> page = GoogleSearchPage(b)
>>> page.load()
>>> page.agree_to_cookies()
>>> page.search('car')
"""

from typing import Any, ClassVar, Tuple, Type

import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

Webdriver = Any
ByObject = Type[selenium.webdriver.common.by.By]


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
    :param webdriver: selenium Webdriver object which can be used to
        interact with the web elements
    :type webdriver: selenium.Webdriver
    """

    url: ClassVar[str] = 'https://google.com'
    search_input: ClassVar[Tuple[ByObject, str]] = (By.NAME, 'q')
    consent_iframe: ClassVar[Tuple[ByObject, str]] = (By.CSS_SELECTOR,
                                                      'div[id=cnsw] iframe')
    agree_button: ClassVar[Tuple[ByObject, str]] = (By.CSS_SELECTOR,
                                                    "div[id=introAgreeButton]")
    english_lang: ClassVar[Tuple[ByObject, str]] = (By.CSS_SELECTOR, 
                                                    "div[id='SIvCob'] a")

    def __init__(self, webdriver: Webdriver) -> None:
        self.webdriver = webdriver

    def load(self) -> None:
        """Loads the search page.
        """
        self.webdriver.get(self.url)

    def agree_to_cookies(self) -> None:
        """Agrees to all cookies to be able to start using the search page.
        """
        frame = self.webdriver.find_element(*self.consent_iframe)
        self.webdriver.switch_to.frame(frame)
        button = self.webdriver.find_element(*self.agree_button)
        button.click()

    def switch_to_english(self) -> None:
        """Changes the language to English.
        """
        link = self.webdriver.find_element(*self.english_lang)
        link.click()

    def search(self, phrase: str) -> None:
        """Initiate a search on the search page with the given phrase.

        :param phrase: Search phrase
        :type phrase: str
        """
        search_input = self.webdriver.find_element(*self.search_input)
        search_input.send_keys(phrase + Keys.RETURN)
