
my_book = {
    "title": "Burn",
    "author": "Ellen Hopkins",
    "year": 2006,
    "rating": 5,
    "pages": 400
}

my_book_list = [
    {
      "title": "Burn",
      "author": "Ellen Hopkins",
      "year": 2006,
      "rating": 5,
      "pages": 400
    },
    {
        "title": "Tricks",
        "author": "Ellen Hopkins",
        "year": 2007,
        "rating": 2.5,
        "pages": 450
    },
    {
        "title": "Twin",
        "author": "Ellen Hopkins",
        "year": 2014,
        "rating": 3.7,
        "pages": 550
    }
]

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def books(book_dictionary):
    
    book_string = f"The name of this book is {book_dictionary['title']}, and was written by {book_dictionary['author']}. It was published in {book_dictionary['year']} and it has a rating of {book_dictionary['rating']}. The book has {book_dictionary['pages']} pages."
    
    return book_string

print(books(my_book))



# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def the_book_title(book_dictionary):
    book_title = book_dictionary["title"]
    return book_title

print(the_book_title(my_book))

def the_book_author(book_dictionary):
    book_author = book_dictionary["author"]
    return book_author

print(the_book_author(my_book))

def the_book_year(book_dictionary):
    book_year = book_dictionary["year"]
    return book_year

print(the_book_year(my_book))

def the_book_rating(book_dictionary):
    book_rating = book_dictionary["rating"]
    return book_rating

print(the_book_rating(my_book))

def the_book_pages(book_dictionary):
    book_pages = book_dictionary["pages"]
    return book_pages

print(the_book_year(my_book))




# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def book_from_list(book_dictionary_list):
    for book_dictionary in book_dictionary_list:
        print(books(book_dictionary))

book_from_list(my_book_list)


def the_authors(book_dictionary_list):
    author_set = set()

    for book_dictionary in book_dictionary_list:
        author_set.add(book_dictionary["author"])

    return author_set

print(the_authors(my_book_list))

def total_pages(book_dictionary_list):
      pages = 0

for book_dictionary in book_dictionary_list:
        pages += book_dictionary["pages"]

        return pages

print(total_pages(my_book_list))

