from app import books, quotes, quotes_web, quotes_js


USER_CHOICE = """
- 'a' show all books
- 'b' show top 10 5-star books
- 'c' to look at cheapest books
- 'n' next available book on the page
- 't' total books
- 'v' view <request> inspirational quotes
- 'w' view <web> inspirational  quotes
- 'j' view <js> inspirational quotes
- 'q' quit

Enter your choice: """


def print_all_books():
    for book in books:
        print(book)


def print_best_books():
    best_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10] # first sort by rating, then by price for similar items
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


books_generator = (e for e in books)


def get_next_book():
    print(next(books_generator))


def total_books():
    print(len(books))


def view_quotes():
    for quote in quotes:
        print(quote)

def web_quotes():
    for quote in quotes_web:
        print(quote)


# NEW menu construct method by passing the menu object
#--------------------------------------------------------------
user_choices = {
    'a': print_all_books,
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book,
    't': total_books,
    'v': view_quotes,
    'w': web_quotes,
    'j': quotes_js
}

def menu():
    choice = input(USER_CHOICE)
    while choice != 'q':
        if choice in ('a','b','c','n','t','v','w','j'):
            user_choices[choice]()
        else:
            print('That is not a valid selection, try again.')
        choice = input(USER_CHOICE)
#--------------------------------------------------------------
# NEW menu items and selection mothod


menu()
