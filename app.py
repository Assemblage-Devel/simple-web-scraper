import requests

from pages.books_page import BooksPage


def quotes_website():
    page_content = requests.get('https://quotes.toscrape.com').content
    page = BooksPage(page_content)

    for quote in page.quotes:
        print(quote) # __repr__ replies


def books_website():
    page_content = requests.get('https://books.toscrape.com/').content
    # print(page_content)
    page = BooksPage(page_content)

    for book in page.books:
        print(book) # __repr__ replies




# quotes_website()
books_website()