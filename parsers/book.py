import re
from locators.book_locators import BookLocators


class BookParser:
    """
    Given a quote div, find the elements (content, author, tags)
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self): # 'represent' from course: (64)
        return f'Book: {self.title}, Price: {self.price}'

    @property
    def title(self):
        locator = BookLocators.TITLE
        return self.parent.select_one(locator)['title']
    
    @property
    def price(self):
        locator = BookLocators.PRICE
        value = self.parent.select_one(locator).string
        expression = '[0-9,]+\.[0-9]+'
        match = re.search(expression, value)
        comma_removed = match.group(0).replace(',','')
        price = float(comma_removed)
        return price
    
    @property
    def rating(self):
        locator = BookLocators.RATING
        return ''