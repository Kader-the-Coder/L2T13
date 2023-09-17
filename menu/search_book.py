"""
This is the only module that can read and return data from database.

This module is responsible for handling what happens if a user decides
to search for a book from the database.

The main goal purpose of this module it to ensure that valid and existing
book_id's are supplied to all other modules that requires them.
"""

#=======================IMPORT LIBRARIES/MODULES=======================
# pylint: disable=import-error

from database.db_read import db_get_books
from display.print_columns import print_columns
from display.clear_lines import clear_lines

# pylint: enable=import-error
#===========================DEFINE FUNCTION============================


def search_book(search_text:str | None = "") -> list:
    """
    Prints a list of books containing a specified search text. The text
    is looked for in all columns unless specified using the @ symbol.

    * search_text (Default None): The text to search for.
       * Omitting this parameter triggers a request for user input.
       * Searches all columns unless search_text starts with:
       * @id: Search in column labelled id
       * @title: Search in column labelled title
       * @author: Search in column labelled author
       * @qty: Search in column labelled qty
    """
    print("* Press ENTER to display all books in database.",
          "* OR input text to display specific books.",
          "  Refine search by specifying column as follows:",
          "  @id <text>, @title <text>, @author <text>, @qty <text>\n",
          sep="\n")

    field_list = ["id", "title", "author", "qty"]
    field_text = "" # For user feedback purposes

    def get_field(search_text:str) -> str:
        """Returns a field from field_list as an index"""
        if len(search_text) > 1:
            # Checks to see if search_text needs to be formatted
            if search_text[0] == "@":
                # Remove @ symbol
                search_text = search_text[1:]
                # Determine keyword by looking at first word.
                search_text = search_text.split()
                if search_text[0].lower() == field_list[0]:
                    return 0
                if search_text[0].lower() == field_list[1]:
                    return 1
                if search_text[0].lower() == field_list[2]:
                    return 2
                if search_text[0].lower() == field_list[3]:
                    return 3
        # If field specified incorrectly or not at all.
        return -1

    # If search_text is not empty:
    if search_text:
        field = get_field(search_text)
        search_text_input = search_text
    else:
        # Request user to enter a text to search:
        search_text_input = input("Search: ")
        field = get_field(search_text_input)
        clear_lines(1)

    # If search_text correctly specifies a field to search in:
    if field != -1:
        # Remove @field from search text before using db_get_books()
        field_text = f"in {field_list[field]} column"
        search_text_input = search_text_input.split()
        search_text_input = "".join(search_text_input[1:])

    # Retrieve a 2D list of books that matches search_text.
    book_list = db_get_books(search_text_input, field)
    
    # If books were successfully retrieved from db_get_books
    if book_list:
        # If search text is empty:
        if not search_text_input:
            search_text_input = "all books in database" # For user feedback purposes

        # Print list of books that matches search text.
        print(f"Showing results for \"{search_text_input}\"",
              field_text)
        print_columns("BOOK LIST",["id", "title", "author", "qty"], book_list)
        return book_list

    print("\nNo book matches your input.")
    return []


#===============================TEST UNIT==============================
if __name__ == '__main__':
    search_book("")
