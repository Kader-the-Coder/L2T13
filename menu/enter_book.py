"""
This module is responsible for handling what happens if a user decides
to enter a new book to the database.

NOTE: This module is run under the assumption that the supplied book_id
      is valid and exists in database.
"""

#=======================IMPORT LIBRARIES/MODULES=======================

from database.db_modify import db_insert    # pylint: disable=import-error

#===========================DEFINE FUNCTION============================

def enter_book(book_title:str, book_author:str) -> None:
    """
    Enters a book with book_title and book_author to database.

    NOTE: id is assigned incrementally
    NOTE: qty why is set to 0
    """
    db_insert(book_title, book_author)
    print("\nBook successfully entered!")

#=============================Test Unit================================

if __name__ == "__main__":
    # As of now, there is no protection as to what can be entered into
    # database from this module.

    enter_book("Foo", "bar")
