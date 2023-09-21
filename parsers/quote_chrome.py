from locators.quote_locators import QuoteLocators
from selenium.webdriver.common.by import By

class QuoteParserChrome:
    """
    Given a quote div, find the elements (content, author, tags)
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self): # 'represent' from course: (64)
        return f'Quote: {self.content}, by Author: {self.author}'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.find_element(By.CSS_SELECTOR, locator).text
    
    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.find_element(By.CSS_SELECTOR, locator).text
    
    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return [t.string for t in self.parent.find_elements(By.CSS_SELECTOR, locator)]


