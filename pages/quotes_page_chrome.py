from typing import List
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote_chrome import QuoteParserChrome, QuoteParserJS

class QuotesPageChrome:
    def __init__(self, browser):
        self.browser = browser
        
    @property
    def quotes(self) -> List[QuoteParserChrome]:
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.browser.find_elements(By.CSS_SELECTOR, locator)
        return [QuoteParserChrome(e) for e in quote_tags]
    
    @property
    def quotes_js(self) -> List[QuoteParserJS]:
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.browser.find_elements(By.CSS_SELECTOR, locator)
        return [QuoteParserJS(e) for e in quote_tags]
    
    @property
    def author_dropdown(self) -> Select:
        locator = QuotesPageLocators.AUTHOR_DROPDOWN
        element = self.browser.find_element(By.CSS_SELECTOR, locator)
        return Select(element)

    @property
    def tags_dropdown(self) -> Select:
        locator = QuotesPageLocators.TAG_DROPDOWN
        element = self.browser.find_element(By.CSS_SELECTOR, locator)
        return Select(element)
    
    @property
    def search_button(self):
        locator = QuotesPageLocators.SEARCH_BUTTON
        button = self.browser.find_element(By.CSS_SELECTOR, locator)
        return button


    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def get_available_tags(self):
        return [tag.text.strip() for tag in self.tags_dropdown.options]

    def select_tag(self, tag: str):
        self.tags_dropdown.select_by_visible_text(tag)