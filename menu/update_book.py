"""
This module is responsible for handling what happens if a user decides
to update an existing new book in the database.

NOTE: This module is run under the assumption that the supplied book_id
      is valid and exists in database.
"""

#=======================IMPORT LIBRARIES/MODULES=======================
# pylint: disable=import-error

from input_check import input_field, input_value
from database.db_modify import db_update
from config import INVALID_SYMBOLS

# pylint: enable=import-error
#===========================DEFINE FUNCTION============================


def update_book(book_id:int) -> None:
    """
    Request user to input the field and new value, then updates the book
    (with book_id) with the new value.

    This module calls the "db_update" function after determining the
    parameters of said function through user input.
    """
    while True:
        # Request user to enter the field that must be updated
        print("Please input either \"title\", \"author\" or \"qty\".")
        field = input_field("Field: ")

        # Determine if updated value must be a text or a number
        value_is_text = "qty" not in field

        print(f"\nPlease enter the new {field}.",
              f"NOTE: {INVALID_SYMBOLS} may not be used.\n",    # pylint: disable=undefined-variable
              sep="\n")
        new_value = input_value(f"{field}: ", value_is_text)

        # Update book.
        db_update(book_id, field, new_value)
        print(f"\n\"{field}\" has been successfully updated to",
              f"\"{new_value}\".")
        break


#=============================Unit Test================================

if __name__ == "__main__":
    # Updating a non-existent book prints the same message as updating
    # an existing book as this module assumes that the supplied id number
    # is valid.
    update_book("be")
