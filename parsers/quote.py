from locators.quote_locators import QuoteLocators


class QuoteParser:
    """
    Given a quote div, find the elements (content, author, tags)
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Quote: {self.content}, by Author: {self.author}'

    @property
    def contnet(self):
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string
    
    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string
    
    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return [t.string for t in self.parent.select(locator)]


