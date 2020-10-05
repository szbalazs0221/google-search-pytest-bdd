"""This module contains step definitions for google_search.feature"""

import selenium.webdriver

from pages.search_page import GoogleSearchPage
from pages.search_results import GoogleSearchResults


def test_search():
    try:
        b = selenium.webdriver.Chrome()
        b.implicitly_wait(10)
        page = GoogleSearchPage(b)
        page.load()
        page.agree_to_cookies()
        page.search('Panda')
        result = GoogleSearchResults(b)
        titles = result.get_result_link_titles()
        assert 'panda' in titles[0]
    except:
        raise
    finally:
        b.close()
