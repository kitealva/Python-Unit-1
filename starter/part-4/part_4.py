### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.
def creation():
    pig = input('What is your book name?: ')
    date = input('When was your book created?: ')
    author = input('Who is the author?: ')
    pages = input('How many pages are in the book?: ')
    rating = input('What is the rating on amazon?: ')
    book = [pig, date, author, pages, rating]
    return book
print(creation())
# Code here


### Step 2 - Type conversion

## Now convert the proper data-types from strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here



### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

