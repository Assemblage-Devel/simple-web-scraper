from bs4 import BeautifulSoup
import re
import logging

from locators.book_page_locators import BookPageLocators
from parsers.book import BookParser

# Takes in entire page content and parses with BeautifulSoup

logger = logging.getLogger('scraping.all_books_page')

class BooksPage:
    def __init__(self, page):
        logger.debug('Parcing page content with BeuatifulSoup HTML parser')
        self.soup = BeautifulSoup(page, 'html.parser')
    
    @property
    def page_count(self):
        logger.debug( f'Finding total page count.')
        locate_pages = BookPageLocators.PAGES
        pages = self.soup.select_one(locate_pages).string
        logger.info(f'Found pages string <{pages}>')
        expression = 'Page 1 of ([0-9]+)'
        match = re.search(expression, pages)
        total_pages = int(match[1])
        logger.debug(f'Extracted number of pages as int <{total_pages}>')
        return total_pages

    @property
    def books(self):
        logger.debug( f'Finding all books on the page using `{BookPageLocators.BOOKS}`.')
        locator = BookPageLocators.BOOKS
        book_tags = self.soup.select(locator)
        return [BookParser(e) for e in book_tags]