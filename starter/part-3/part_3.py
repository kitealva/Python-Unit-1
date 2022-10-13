my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def book_stuff(book):
    return f"{book['title']} is made by {book['author']} in {book['year']} and has a rating of {book['rating']} with a total page length of {book['pages']} pages."

print(book_stuff(my_book))


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def book_info1(cow):
    return f"{cow['author']}"

def book_info2(bacca):
    return f"{bacca['title']}"

def book_info3(kore):
    return f"{kore['year']}"

print(book_info3(my_book))
# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def book_author(book):
    return book['author']

def book_rating(book):
    return book['rating']

def book_pages(book):
    return book['pages']

print(book_rating(my_book))