__author__ = 'jc457651'

# Initialize the constants
# https://github.com/jc457651/assignment1.git

FILE = "books.csv"


def main():
    print("Reading List 1.0 - by Harpreet Kaur")
    book_list = []
    load_books(book_list)
    print(book_list)
    display_menu()
    choice = input(">>>")
    while choice.lower() != 'q':
        if choice.lower() == 'r':
            required_books(book_list)
        elif choice.lower() == 'c':
            completed_books(book_list)
        elif choice.lower() == 'a':
            book_list= add_books()
        elif choice.lower() == 'm':
            complete_a_book(book_list)
        else:
            print("Invald menu choice")
        display_menu()
        choice = input(">>>")
    print("{} books have been saved to {}".format(len(book_list),FILE))
    print("Have a nice day :)")


def display_menu():
    """
    This function is used to display the options Menu
"""
    MENU = "Menu: \nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as " \
           "completed\nQ - Quit"
    print(MENU)


# After the display_menu function
"""
     This will load books from file to List
     filebook <- open(FILE,'r')
     for line in book:
        booksappend(line.strip().split(','))
    end of for loop
    close the file by filebook.close()
ENDFUNCTION

"""
def load_books(book_list):

    book_file = open(FILE, 'r')
    for line in book_file:
        book_list.append(line.strip().split(','))
    book_file.close()


# After the load_books()


def complete_a_book(book_list):
    """
    This Function will complete a book into a file
    ask from the user to enter a number of books to mark as completed
    check the condition while check=0
    in try
     number_of_books = int(input(">>>"))
        if book_list[number_of_books][3] == 'c':
            it will display that book is already completed
        else
             book_list[number_of_books][3] = 'c'
            books_file = open(FILE, 'w')
            for i in book_list:
                for j in i:
                    if j == "r" or j == "c":
                        print(j, end='', file=books_file)
                    else:
                        print(j, end=',', file=books_file)
                print(file=books_file)
                close the file by  books_file.close()
                it will display title by author is completed
                check if it is 1
                except ValueError:
                it will display invalid number and enter a valid number


"""
    required_books(book_list)
    print("Enter the number of a book to mark as completed")
    try:
        number_of_books = int(input(">>>"))
        if book_list[number_of_books][3] == 'c':
            print("That book is already completed")
        else:
            book_list[number_of_books][3] = 'c'
            books_file = open(FILE, 'w')
            for i in book_list:
                for j in i:
                    if j == "r" or j == "c":
                        print(j, end='', file=books_file)
                    else:
                        print(j, end=',', file=books_file)
                print(file=books_file)
            books_file.close()
            print("{} by {} is completed".format(book_list[number_of_books][0], book_list[number_of_books][1]))
    except ValueError:
        print("Invalid input; Enter a valid number")
        complete_a_book(book_list)


# After the complete function

def required_books(book_list):
    """
    This function will show the list of books which we want to read
"""
    total_pages = 0
    print("Required Books:")
    count = 0
    count1=0
    print(book_list)
    for i in book_list:
        if 'r' in book_list[count][3]:
            print("{}. {:<50s} by {:<20s} {:>15s} pages".format(count, book_list[count][0], book_list[count][1],
                                                                book_list[count][2]))
            total_pages += int(book_list[count][2])
            count1 = count1+1
        count += 1
    if count != 0:
        print("Total pages for {} books: {}".format(count1 , total_pages))
    else:
        print("No books")


# end of required_books function

def completed_books(book_list):
    """
    This function will list or show all the List of completed books
"""
    total_pages = 0
    print("Completed Books:")
    count = 0
    count1=0
    for i in book_list:
        if 'c' in book_list[count][3]:
            print("{}. {:<50s} by {:<20s} {:>15s} pages".format(count, book_list[count][0], book_list[count][1],
                                                                book_list[count][2]))
            total_pages += int(book_list[count][2])
            count1 = count1+1
        count += 1
    print("Total pages for {} books: {}".format(count1 , total_pages))


# After the completed_books function

def add_books():
    """
    This function will add books into the file books.csv
"""
    title = input("Title:")
    while title == "":
        print("Input can not be blank")
        title = input("Title:")
    author = input("Author:")
    while author == "":
        print("Input can not be blank")
        author = input("Author:")
    flag = 0
    pages = 0
    while flag == 0:
        try:
            pages = int(input("Pages: "))
            while pages <= 0:
                print("Number must be >= 0")
                pages = int(input("Pages: "))
            flag = 1
        except ValueError:
            print("Invalid input; Enter a valid number")
    print("{} by {}, ({} pages) added to reading list".format(title, author, pages))
    book = [title, author, str(pages), 'r']
    book_list = []
    load_books(book_list)
    book_list.append(book)
    print(book_list)
    books_file = open(FILE, 'w')
    for i in book_list:
        for j in i:
            if j == "r" or j == "c":
                print(j, end='', file=books_file)
            else:
                print(j, end=',', file=books_file)
        print(file=books_file)
    books_file.close()
    return book_list


# end of add_books function

def save_books(books):
    """
    This function will save books into the file books.csv
"""
    


# end of save book function
main()
