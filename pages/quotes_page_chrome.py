from typing import List
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote_chrome import QuoteParserChrome

class QuotesPageChrome:
    def __init__(self, browser):
        self.browser = browser
        
    @property
    def quotes(self) -> List[QuoteParserChrome]:
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.browser.find_elements(By.CSS_SELECTOR, locator)
        return [QuoteParserChrome(e) for e in quote_tags]