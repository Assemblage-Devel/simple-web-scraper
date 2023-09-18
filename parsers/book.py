import re
from locators.book_locators import BookLocators


DOMAIN = 'https://books.toscrape.com/'
RATINGS = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}


class BookParser:
    """
    Given a quote div, find the elements (content, author, tags)
    """
    DOMAIN = 'https://books.toscrape.com/'
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5   
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self): # 'represent' from course: (64)
        return f'Book: {self.title}, link: {self.link} ({self.rating} stars) Price: {self.price}'

    @property
    def title(self):
        locator = BookLocators.TITLE
        return self.parent.select_one(locator)['title'] # or .attrs['title']
     
    @property
    def link(self):
        locator = BookLocators.LINK
        return f"{BookParser.DOMAIN}{self.parent.select_one(locator).attrs['href']}" # IMPORTANT doesnt return error for none
    
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
        value = self.parent.select_one(locator).attrs['class'] # [star-rating, Three]
        rating = [p for p in value if p != 'star-rating']
        return BookParser.RATINGS.get(rating[0], '-') # IMPORTANT doesnt return error for none
