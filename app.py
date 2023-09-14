import requests

from pages.quotes_page import QuotesPage


page_content = requests.get('https://quotes.toscrape.com').content
page = QuotesPage(page_content)

print(page.quotes)