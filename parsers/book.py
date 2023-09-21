import re
import logging
from locators.book_locators import BookLocators


logger = logging.getLogger('scraping.book_parser')

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
        logger.debug(f'New book parser created from <{parent}>')
        self.parent = parent

    def __repr__(self): # 'represent' from course: (64)
        return f'Book: {self.title}, link: {self.link} ({self.rating} stars) Price: {self.price}'

    @property
    def title(self):
        logger.debug('Finding book name..')
        locator = BookLocators.TITLE
        title = self.parent.select_one(locator).attrs['title']
        logger.debug(f'Found title <{title}>')
        return title
     
    @property
    def link(self):
        logger.debug('Finding book link..')
        locator = BookLocators.LINK
        link = f"{BookParser.DOMAIN}{self.parent.select_one(locator).attrs['href']}" # IMPORTANT doesnt return error for none
        logger.debug(f'Found link <{link}>')
        return link
    
    @property
    def price(self):
        logger.debug('Finding book price..')
        locator = BookLocators.PRICE
        value = self.parent.select_one(locator).string
        expression = '[0-9,]+\.[0-9]+'
        match = re.search(expression, value)
        comma_removed = match.group(0).replace(',','')
        price = float(comma_removed)
        logger.debug(f'Found price <{price}>')
        return price
    
    @property
    def rating(self):
        logger.debug('Finding book rating..')
        locator = BookLocators.RATING
        value = self.parent.select_one(locator).attrs['class'] # [star-rating, Three]
        rating = [p for p in value if p != 'star-rating']
        logger.debug(f'Found rating <{rating}>')
        return BookParser.RATINGS.get(rating[0], '-') # IMPORTANT doesnt return error for none
