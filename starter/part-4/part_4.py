### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.
# from secrets import choice
# from turtle import title


# def creation():
#     pig = input('What is your book name?: ')
#     date = input('When was your book created?: ')
#     author = input('Who is the author?: ')
#     pages = input('How many pages are in the book?: ')
#     rating = input('What is the rating on amazon?: ')
#     book = [pig, date, author, pages, rating]
#     return book
# print(creation())
# # Code here


### Step 2 - Type conversion

## Now convert the proper data-types from strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def creation():
#     pig = input('What is your book name?: ')
#     date = int(input('When was your book created?: '))
#     author = input('Who is the author?: ')
#     pages = int(input('How many pages are in the book?: '))
#     rating = float(input('What is the rating on amazon?: '))
#     book = [pig, date, author, pages, rating]
#     return book
# print(creation())
### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# def creation():
#     pig = input('What is your book name?: ')
#     try:
#         date = int(input('When was your book created?: '))
#     except:
#         date = int(input("Enter a number: "))
#     author = input('Who is the author?: ')
#     try:
#         pages = int(input('How many pages are in the book?: '))
#     except:
#         pages = int(input("Tell me how many pages there are: "))
#     try:
#         rating = float(input('What is the rating on amazon?: '))
#     except:
#         rating = float(input("What is your rating out of 5?: "))
#     book = [pig, date, author, pages, rating]
#     return book
# print(creation())

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
# def main_menu(books):
#     choice = input("Choose 1 to add book. Choose 2 to see books. Choose 3 to leave.:")
    
#     if choice == '1':
#         books.append(create_new_book())
#     elif choice == '2':
#         print_all_books(books)
#     elif choice == '3':
#         print("\nLeaving")
#         active = False
#     else:
#         print("\nNumber is invalid choose 1,2,3.\n")

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here
current_books = [
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "date": 1997,
        "rating": 4.5,
        "pages": 309
    },
    {
        "title": "Twilight",
        "author": "Stephenie Meyer",
        "date": 2005,
        "rating": 3.6,
        "pages": 498
    },
    {
        "title": "The Fault in Our Stars",
        "author": "John Green",
        "date": 2012,
        "rating": 4.2,
        "pages": 313
    },
    {
        "title": "Divergent",
        "author": "Veronica Roth",
        "date": 2011,
        "rating": 4.2,
        "pages": 487
    }
]

def creation():
    title = input('What is your book name?: ')
    author = input('Who is the author?: ')
    try:
        date = int(input('When was your book created?: '))
    except:
        date = int(input('Type a number:'))
    try:
        rating = float(input('What is the rating on amazon?: '))
    except:
        rating = float(input('What would you rate this book?: '))
    try:
        pages = int(input('How many pages are in the book?: '))
    except:
        pages = int(input('Number of pages?: '))
        

    book_dictionary = {
        "title": title,
        "author": author,
        "date": date,
        "rating": rating,
        "pages": pages
    }
    
    return book_dictionary

def print_all_books(books):
    
    print("Here are all the books...")
    
    for book in books:
        title = book["title"]
        author = book["author"]
        date = book["date"]
        rating = book["rating"]
        pages = book["pages"]
        
        print(f"Title: {title}, Author: {author}, Date: {date}, Rating: {rating}, Pages: {pages}")
        
def main_menu(book_source):
    
    active = True
    
    while active:
        choice = input("\nChoose 1 to add a book...\nChoose 2 to see all books...\nChoose 3 to how many books you have...\nChoose 4 to see how many pages in books...\nChoose 5 to leave.\nType here: ")
        
        if choice == "1":
            book_source.append(creation())
        elif choice == "2":
            print_all_books(book_source)
        elif choice == "3":
            print(f"\nYou have a total of {len(book_source)} books.\n")
        elif choice == "4":
            print(f"\nYou books page count totals {sum([x['pages'] for x in book_source])} pages!\n")
        elif choice == "5":
            print("\nGoodbye")
            active = False
        else:
            print("\nSorry please type a number for one of the options.\n")

main_menu(current_books)