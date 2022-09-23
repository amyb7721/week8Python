### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

def create_new_book(book_source):
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
       
    with open(book_source, "a") as file:
        file.write(f"{title}, {author}, {year}, {pages}, {rating}\n")



### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

def original_book(book_source):

     print("\nHeres all your books\n")
    
     with open(book_source, "r") as f:
         file = f.readlines()
        
         for line in file:
             title, author, year, pages, rating = line.split(", ")

             print(f"Title: {title}, Author: {author}, Year: {year}, Pages: {pages}, Rating: {rating}")



### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!



def books_list_of_dictionaries(book_source):
    books_list = []
    with open(book_source, "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, pages, rating = line.split(", ")
            books_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "pages": int(pages),
                "rating": float(rating),
            })
    return books_list

def book_printed(book):
    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Pages: {book['pages']}, Rating: {book['rating']},")

def view_books(book_source):
    print("\nHeres all your books\n")
    for book in books_list_of_dictionaries(book_source):
        book_printed(book)

def highest_rated(book_source):
    list = books_list_of_dictionaries(book_source)
    return max(list, key=lambda x: int(x["rating"]))

def lowest_rated(book_source):
    list = books_list_of_dictionaries(book_source)
    return min(list, key=lambda x: int(x["rating"]))

def sorted_list_rating(book_source):
    print("\nHeres all your ranked by rating\n")
    list = books_list_of_dictionaries(book_source)
    list =  sorted(list, key=lambda x: int(x["rating"]), reverse = True)
    for book in list:
        book_printed(book)

def main_menu(book_source):

    active = True

    while active:
        choice = input("""
Choose 1 to add a book
Choose 2 to see all your books
Choose 3 to see a count of your books
Choose 4 to see a count of the pages of your books
Choose 5 to see the your highest rated book
Choose 6 to see your lowest rated book
Choose 7 to see your books ranked by order of rating
Choose 0 to exit.
Type here: """)

        if choice == "1":
            create_new_book(book_source)
        elif choice == "2":
            view_books(book_source)
        elif choice == "3":
            print(f"\nYou have  {len(books_list_of_dictionaries(book_source))} books.\n")
        elif choice == "4":
            print(f"\nBook has  {sum([x['pages'] for x in books_list_of_dictionaries(book_source)])} pages!\n")
        elif choice == "5":
            print("\nHighest rated book\n")
            book_printed(highest_rated(book_source))
        elif choice == "6":
            print("\nLowest rated book\n")
            book_printed(lowest_rated(book_source))
        elif choice == "7":
            sorted_list_rating(book_source)
        elif choice == "0":
            print("\nExiting Out")
            active = False
        else:
            print("\nType a number for one of the options.\n")

main_menu("library.txt")