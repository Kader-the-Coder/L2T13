"""
!!!!!!!!!!!!!Running this module resets "books_db" database!!!!!!!!!!!!

This module is responsible for creating and interacts with the "books_db"
database.

NOTE: Running this module resets database back to its default values.
      I.e. Will create "data\\books_db" if missing and populate
      "books_db" with tables and table values specified in task.

"db_execute" is the main function in this module and is imported and
called by all other modules and functions with the prefix 'db_'.
"""

#=======================IMPORT LIBRARIES/MODULES=======================

import os
import sys
import sqlite3

#=========================INITIALIZE VARIABLES=========================

# Set directory relative to main file
directory = os.path.dirname(__file__)
books_db = os.path.join(directory, 'data/books_db')

#===========================DEFINE FUNCTIONS===========================


def db_execute(query:str, parameters:str | None = "") -> list[any]:
    """
    Returns a list of values obtained from executing a given query.

    * query: The query to execute on cursor.
    * parameters (Default ""): The parameters to apply when query is a
      prepared statement.
    """
    try:
        database = sqlite3.connect(books_db)
        cursor = database.cursor()
        cursor.execute(query, parameters)
        database.commit()
        return cursor.fetchall()

    except sqlite3.OperationalError as err:
        print(f'Oops, looks like something went wrong.\n{err}')
        print('Program will now terminate.')
        sys.exit()

    finally:
        cursor.close()
        database.close()


def db_reset() -> None:
    """Resets database back to its default values"""

    def create_directory():
        """
        Create data folder containing books_bk in current directory.
        """
        if not os.path.isdir(os.path.join(directory,'data')):
            os.makedirs(os.path.join(directory,'data'))


    def create_tables():
        """Create inventory and books table"""
        db_execute('''
            CREATE TABLE inventory (
                    id INTEGER,
                    qty INTEGER,
                    PRIMARY KEY (id)
                    )
                    ''')
        db_execute('''
            CREATE TABLE books (
                    id INTEGER,
                    title TEXT,
                    author TEXT,
                    PRIMARY KEY (id)
                    FOREIGN KEY (id) REFERENCES inventory(id))
                    ''')


    def populate_table():
        """
        Populate inventory and books table with default values as
        specified in task. This function can be repurposed in later
        versions to read from a file when importing books from an
        existing system.
        """
        id_list = [3001, 3002, 3003, 3004, 3005]
        qty_list = [30, 40, 25, 37, 12]
        author_list = ["Charles Dickens" ,
                    "J.K. Rowling",
                    "C. S. Lewis",
                    "J.R.R Tolkien",
                    "Lewis Carroll"]
        title_list = ["A Tale of Two Cities",
                    "Harry Potter and the Philosopher's Stone",
                    "The Lion, the Witch and the Wardrobe",
                    "The Lord of the Rings",
                    "Alice in Wonderland"]

        for i, id_num in enumerate(id_list):
            db_execute('''INSERT INTO inventory(id, qty)
                VALUES (?,?)''', (id_num, qty_list[i]))
            db_execute('''INSERT INTO books(id, title, author)
                VALUES (?,?,?)''', (id_num, title_list[i], author_list[i]))


    create_directory()
    db_execute('DROP TABLE IF EXISTS books')
    db_execute('DROP TABLE IF EXISTS inventory')
    create_tables()
    populate_table()


#===============================UNIT TEST==============================
if __name__ == '__main__':
    db_reset()
