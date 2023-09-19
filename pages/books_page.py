from bs4 import BeautifulSoup
import re

from locators.book_page_locators import BookPageLocators
from parsers.book import BookParser

# Takes in entire page content and parses with BeautifulSoup

class BooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')
    
    @property
    def page_count(self):
        locate_pages = BookPageLocators.PAGES
        pages = self.soup.select_one(locate_pages).string
        expression = 'Page 1 of ([0-9]+)'
        match = re.search(expression, pages)
        total_pages = int(match[1])
        return total_pages

    @property
    def books(self):
        locator = BookPageLocators.BOOKS
        book_tags = self.soup.select(locator)
        return [BookParser(e) for e in book_tags]