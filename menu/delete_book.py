"""
This module is responsible for handling what happens if a user decides
to delete a book from the database.

The main goal is to ensure that a user is sure if they want to delete a
book.
NOTE: This module is run under the assumption that the supplied book_id
      is valid and exists in database.
"""
#=======================IMPORT LIBRARIES/MODULES=======================

from database.db_modify import db_delete    # pylint: disable=import-error

#===========================DEFINE FUNCTION============================


def delete_book(book_id:int) -> None:
    """Deletes a book (by id) upon user confirmation."""
    print("Are you sure you want to delete this book?",
          "Input either Yes or No.")
    confirm_delete = input(": ")

    if confirm_delete.lower() == "yes":
        db_delete(book_id)
        print(f"Book with id {book_id} has been successfully deleted.")
    else:
        print("Deletion of book has been canceled.\n")


#=============================Test Unit================================

if __name__ == "__main__":
    # Deleting a non-existent book prints the same message as deleting
    # an existing book as this module assumes that the supplied id number
    # is valid.
    delete_book("asd")
