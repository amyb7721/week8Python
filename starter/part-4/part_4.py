### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

title = input("What is the title of the book? - ")
author = input("Who is the author of the book? - ")
year = input("What year was this book published? - ")
pages = input("How many pages does this book have? - ")
rating = input("What rating would you give this book? - ")




### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

title = input("What is the title of the book? - ")
author = input("Who is the author of the book? - ")
year = int(input("What year was this book published? - "))
pages = int(input("How many pages does this book have? - "))
rating = float(input("What rating would you give this book? - "))



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

title = input("What is the title of the book? - ")
author = input("Who is the author of the book? - ")
#try:
year = int(input("What year was this book published? - "))
#except:
year = int(input("Type a number. - "))
# try:
pages = int(input("How many pages does this book have? - "))
# except:
pages = int(input("Type a number. - "))
# try:
rating = float(input("What rating would you give this book? - "))
# except:
rating = int(input("Type a number. - "))


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

def main_menu(books_source):

    choices = input("Pick 1 to see all books. Pick 2 to add a book. Pick 3 to exit out. - ")

    if choices == "1":
         all_books(books_source)
    elif choices == "2":
         books_source.append(new_book())
    elif choices == "3":
         print("\nExiting Out")
         active = False
    else:
         print("\nType a number for one of the options.\n")




### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

current_books = [
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
    },
    {
        "title": "Fallout",
        "author": "Ellen Hopkins",
        "year": 2012,
        "rating": 4.5,
        "pages": 523
    }
]

def new_book():
    title = input("What is the title of the book? - ")
    author = input("Who is the author of the book? - ")
    try:
        year = int(input("What year was this book published? - "))
    except:
        year = int(input("Type a number. - "))
    try:
        pages = int(input("How many pages does this book have? - "))
    except:
        pages = int(input("Type a number. - "))
    try:
        rating = float(input("What rating would you give this book? - "))
    except:
        rating = int(input("Type a number. - "))
   


    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "pages": pages,
        "rating": rating,
    }
    
    return book_dictionary

def all_books(list_of_books):

    print("\nHere are all your books...\n")

    for book in list_of_books:
        title = book["title"]
        author = book["author"]
        year = book["year"]
        pages = book["pages"]
        rating = book["rating"]

        print(f"Title: {title}, Author: {author}, Year: {year}, Pages: {pages}, Rating: {rating}")


def main_menu(books_source):

    active = True

    while active:
        choice = input("\nChoose 1 see all books...\nChoose 2 to add book...\nChoose 3 Exit Out...\n")

        if choice == "1":
            books_source.append(new_book())
        elif choice == "2":
            all_books(books_source)
        elif choice == "3":
             print("\nExiting Out")
             active = False
        else:
            print("\nType a number for one of the options.\n")

main_menu(current_books)
