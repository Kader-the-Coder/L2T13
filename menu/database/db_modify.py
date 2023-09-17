"""
This module is responsible for executing prepared statements which
modifies the database
"""

#=======================IMPORT LIBRARIES/MODULES=======================

from db_execute import db_execute   # pylint: disable=import-error

#===========================DEFINE FUNCTIONS===========================


def db_insert(title:str, author:str) -> None:
    """
    Inserts a book with title and author to "books_db" database
    NOTE: id number is assigned incrementally.
    NOTE: qty is set to 0.
    """
    db_execute('''INSERT INTO inventory(qty)
                  VALUES (0)''')
    db_execute('''INSERT INTO books(title, author)
                  VALUES (?,?)''',
                  (title, author))


def db_update(book_id:int, field:str, new_value:int|str) -> None:
    """
    Updates a book (by id) with a given value in a given field.

    * book_id: The row to update
    * field: The column to update ("qty", "title", "author")
    * new_value: The new value to set.
       * If field = "qty", then new_value = positive integer.
       * If field = "title"|"author", then new_value = string.
    """

    def update_qty(book_id:int, book_qty:int) -> None:
        """Updates the "qty" of a book (by id) to "book_qty"."""
        db_execute('''UPDATE inventory
                    SET qty = ?
                    WHERE id = ?;''',
                    (book_qty, book_id))


    def update_title(book_id:int, book_title:str) -> None:
        """Updates the "title" of a book (by id) to "book_title"."""
        db_execute('''UPDATE books
                    SET title = ?
                    WHERE id = ?;''',
                    (book_title, book_id))


    def update_author(book_id:int, book_author:str) -> None:
        """Updates the "author" of a book (by id) to "book_author"."""
        db_execute('''UPDATE books
                    SET author = ?
                    WHERE id = ?;''',
                    (book_author, book_id))


    if field == "qty":
        update_qty(book_id, new_value)
    elif field == "title":
        update_title(book_id, new_value)
    elif field == "author":
        update_author(book_id, new_value)


def db_delete(book_id:int) -> None:
    """
    Deletes a book (by id) from the database.

    NOTE: There are two execute functions as the database contains two
          tables.
    """
    db_execute('''DELETE FROM books WHERE id=?''', (book_id,))
    db_execute('''DELETE FROM inventory WHERE id=?''', (book_id,))


#===============================UNIT TEST==============================
if __name__ == '__main__':
    db_update(3001, "qty", 10)
    db_update(3002, "title", "Romeo and Juliet")

    # non-existent id numbers will not be updated
    db_update(29, "author", "Donal Trump")
