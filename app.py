import requests
import aiohttp
import logging
import time
import os
from selenium import webdriver

from pages.books_page import BooksPage
from pages.quotes_page import QuotesPage
from pages.quotes_page_chrome import QuotesPageChrome


logging.basicConfig(level=logging.INFO,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")
logger = logging.getLogger("scraping")
logger.info('Loading content ...')


chrome = webdriver.Chrome()
chromejs = webdriver.Chrome()

# Quotes via Chrome
#----------------------------------------------------------------------
chrome.get('https://quotes.toscrape.com')
web_page = QuotesPageChrome(chrome)
quotes_web = web_page.quotes


# JAVASCRIPT Quotes via Chrome
#----------------------------------------------------------------------
chromejs.get('https://quotes.toscrape.com/search.aspx')
js_page = QuotesPageChrome(chromejs)
quotes_js = js_page.search_for_quotes


# Quotes via requests
#-----------------------------------------------------------------------
print('started timing event..')
start = time.time()
quote_page_content = requests.get('https://quotes.toscrape.com').content
quote_page = QuotesPage(quote_page_content)
quotes = quote_page.quotes
print(f'quotes page time: {time.time()-start}')

# Books via requests
#------------------------------------------------------------------------------------------
book_page_content = requests.get('https://books.toscrape.com/catalogue/page-1.html').content
book_page = BooksPage(book_page_content)

print('started timing event..')
start = time.time()
books = book_page.books

for page in range(1, book_page.page_count):
    url = f'https://books.toscrape.com/catalogue/page-{page+1}.html'
    book_page_content = requests.get(url).content
    book_page = BooksPage(book_page_content)
    books.extend(book_page.books)
#------------------------------------------------------------------------------------------
print(f'books page time: {time.time()-start}')

