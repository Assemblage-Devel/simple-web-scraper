from app import books, quotes


USER_CHOICE = """
- 'b' to look at 5-star books
- 'c' to look at cheapest books
- 'n' next available book on the page
- 'v' view inspirational quotes
- 'q' quit

Enter your choice: """

def print_best_books():
    best_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10] # first sort by rating, then by price for similar items
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)
    for book in cheapest_books:
        print(book)


books_generator = (e for e in books)

def get_next_book():
    print(next(books_generator))


def view_quotes():
    for quote in quotes:
        print(quote)



def menu():
    choice = input(USER_CHOICE)

    while choice != 'q':
        if choice == 'b':
            print_best_books()
        elif choice == 'c':
            print_cheapest_books()
        elif choice == 'n':
            print(get_next_book())
        elif choice == 'v':
            view_quotes()
        else:
            print('That is not a valid selection, try again.')
        choice = input(USER_CHOICE)


menu()
