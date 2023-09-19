import requests

from pages.books_page import BooksPage
from pages.quotes_page import QuotesPage


quote_page_content = requests.get('https://quotes.toscrape.com').content
quote_page = QuotesPage(quote_page_content)
quotes = quote_page.quotes

book_page_content = requests.get('https://books.toscrape.com/catalogue/page-1.html').content
book_page = BooksPage(book_page_content)

books = book_page.books

for page in range(1, book_page.page_count):
    url = f'https://books.toscrape.com/catalogue/page-{page+1}.html'
    book_page_content = requests.get(url).content
    book_page = BooksPage(book_page_content)
    books.extend(book_page.books)



