import re
from locators.book_locators import BookLocators


domain = 'https://books.toscrape.com/'

class BookParser:
    """
    Given a quote div, find the elements (content, author, tags)
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self): # 'represent' from course: (64)
        return f'Book: {self.title}, link: {self.link}, rating: {self.rating} Price: {self.price}'

    @property
    def title(self):
        locator = BookLocators.TITLE
        return self.parent.select_one(locator)['title'] # or .attrs['title']
     
    @property
    def link(self):
        locator = BookLocators.LINK
        return f"{domain}{self.parent.select_one(locator)['href']}" # or .attrs['title']
    
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
        value = self.parent.select_one(locator)['class'] # [star-rating, Three]
        print(value)
        # list comprehention is better
        rating = [p for p in value if p != 'star-rating']
        return rating[0]