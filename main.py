"""
Program for a bookstore. This program allow a clerk to enter data about
new books into the database, update book information, delete books from
the database, and search to find the availability of books in the
database.
"""

#=======================IMPORT LIBRARIES/MODULES=======================
# pylint: disable=import-error
# pylint: disable=no-name-in-module

from menu.config import PROGRAM_NAME, INVALID_SYMBOLS, MAIN_MENU
from menu.database.db_execute import db_reset
from menu.input_check import input_value
from menu.delete_book import delete_book
from menu.enter_book import enter_book
from menu.search_book import search_book
from menu.update_book import update_book
from menu.display.clear_lines import clear_lines

# pylint: enable=import-error
#===========================DEFINE FUNCTIONS===========================


def print_header() -> None:
    """Prints the company header on top of terminal"""
    clear_lines(-1)
    print(PROGRAM_NAME, "\n")


def sub_menu_refine_search(refine:bool = True):
    '''
    Present user with option to exit a "search loop".

    * refine(Default True): If additional text must be displayed.
    '''
    if refine:
        print("Refine search until only one book is selected.\n")

    menu = input("Input \"@back\" to return to main menu.\n\n"
                 "Search: ")
    return menu


def menu_search_book(search:str = ""):
    '''
    Calls the search_book function to request what to search for.
    * search: initializes search variable without interfering with loop.
    '''
    while True:
        print_header()
        search_book(search)
        # Create loop to continually search for books
        search = sub_menu_refine_search(False)
        # Return to main menu
        if search == "@back":
            break


def menu_update_book(search:str = ""):
    """
    Calls the search_book function to request what to search for.
    When search results in only 1 book, calls functions to update
    a specified field with a given value for that book.

    * search: initializes search variable without interfering with loop.
    """
    while True:
        print_header()
        # Get list of books matching search criteria.
        book = search_book(search)
        if len(book) == 1:
            update_book(str(book[0][0]))
            input("Press ENTER to return to main menu.")
            break
        # If search does not yield one result
        search = sub_menu_refine_search()
        # Return to main menu
        if search == "@back":
            break


def menu_delete_book(search:str = ""):
    '''
    Calls the search_book function to request what to search for.
    When search results in only 1 book, calls functions to delete
    returned book.

    * search: initializes search variable without interfering with loop.
    '''
    while True:
        print_header()
        # Get list of books matching search criteria.
        book = search_book(search)
        if len(book) == 1:
            delete_book(str(book[0][0]))
            input("Press ENTER to return to main menu.")
            break
        # If search does not yield one result
        search = sub_menu_refine_search()
        # Return to main menu
        if search == "@back":
            break


def menu_enter_book() -> None:
    """
    Requests a book tittle and author and then calls all functions
    involved in entering a new book to the database.
    """
    print_header()
    print("Entering a new book...:\n",
            "Please complete the fields below:",
            f"NOTE: {INVALID_SYMBOLS} may not be used.\n",    
            sep="\n")
    book_title = input_value(" Title: ")
    book_author = input_value("Author: ")
    enter_book(book_title, book_author)
    input("\nPress ENTER to return to main menu.")


def menu_main() -> bool:
    """
    Returns True unless user inputs 0.

    This function deals with user navigation and directly or indirectly
    calls all other functions in this project.
    """
    print_header()
    print(MAIN_MENU)
    menu = [menu_enter_book, menu_update_book,
            menu_delete_book, menu_search_book]
    try:
        option = int(input(""))
        # Exit program
        if option == 0:
            return False

        # This block is for develop mode (Not implemented)
        if option == -1:
            print("\nReset database? Input y or n.")
            option = input(":")
            if option == "y":
                db_reset()
                print("Database has been reset.")
                input("Press ENTER to return to main menu.")
            return True
        
        # Run user-selected function from list.
        menu[option - 1]()
        return True

    except ValueError:
        input("Incorrect input. press ENTER to try again.")
        return True
    except IndexError:
        input("Incorrect input. press ENTER to try again.")
        return True
    except KeyboardInterrupt:
        # This exception acts as an advance feature which mimics
        # pressing the 'ESC' button in most programs.
        return True
    
    # If .\menu\database\data\books_db is missing:
    except UnboundLocalError:
        print("\nFile error! The database containing book information",
              "is missing.",
              "\nReset database? This wll delete all previously inputted data.")
        option = input(":")
        if option.lower() in ["y", "yes", "ok"]:
            db_reset()
            print("Database has been reset.")
            input("Press ENTER to return to main menu.")
        else:
            input("Press ENTER to return to main menu.")
        return True


#===========================MAIN MENU==================================

# Execute main loop.
while menu_main():
    pass

# Print before closing program.
print_header()
print(f"Thank you for using the {PROGRAM_NAME}!",
        "See you again soon.\n")
