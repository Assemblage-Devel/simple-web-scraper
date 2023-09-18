import requests

from pages.books_page import BooksPage
from pages.quotes_page import QuotesPage


quote_page_content = requests.get('https://quotes.toscrape.com').content
quote_page = QuotesPage(quote_page_content)
quotes = quote_page.quotes


book_page_content = requests.get('https://books.toscrape.com/').content
book_page = BooksPage(book_page_content)
books = book_page.books




