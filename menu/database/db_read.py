"""
This module is responsible for executing prepared statements which
reads and returns data from database.
"""

#=======================IMPORT LIBRARIES/MODULES=======================

from db_execute import db_execute   # pylint: disable=import-error

#===========================DEFINE FUNCTIONS===========================


def db_get_books(search_text:str, field:int | None = -1) -> list:
    """
    Returns a 2D list of all books that matches the supplied search_text.

    Example list structure:    
    [[id, title, author, qty], [id, title, author, qty], ...]

    * search_text: The text (case-insensitive) to search for.
    * field (Default -1): The column index to search in.
       * if field == -1 Search in all columns
       * if field == 0 Search in column labelled id
       * if field == 1 Search in column labelled title
       * if field == 2 Search in column labelled author
       * if field == 3 Search in column labelled qty
    
    NOTE: "search_text" is formatted to %search_text% which is seen by
          sqlite3 as a wild card. This allows for partial searching.
    NOTE: a "search_list" is created when a field index is specified. The
          list contains an index value of the formatted search_text for
          each field and then is modified to only contain the search_text in
          the specified field index. The other indexes are then set to "".
    """
    search_text = search_text.strip()

    # Return all books in database.
    if search_text == "":
        book = db_execute('''SELECT *
                            FROM inventory AS i
                            INNER JOIN books AS b
                            ON i.id = b.id''')
    else:
        # Formats 'search_text' to wildcard.
        search_text = f"%{search_text}%"
        search_list = [search_text, search_text, search_text, search_text]

        # If a valid field is specified:
        if 0 <= field <= len(search_list):
            # Format all unspecified fields to ""
            search_list = ["" if i != field else ele for i, ele in enumerate(search_list)]

        # Create a list of tuples with partial matches to 'search_text'.
        book = db_execute('''SELECT *
                            FROM inventory AS i
                            INNER JOIN books AS b
                            ON i.id = b.id
                            WHERE i.id LIKE ?
                            OR title LIKE ?
                            OR author LIKE ?
                            OR qty LIKE ?
                            ''',
                            (search_list[0],
                            search_list[1],
                            search_list[2],
                            search_list[3]))
    # Concatenate tuples to 2D list.
    book = [list(tup) for tup in book]

    # Pop duplicate id number from all lists.
    _ = [x.pop(2) for x in book]
    for ele in book:
        ele[1],ele[3] = ele[3],ele[1]
        ele[1],ele[2] = ele[2],ele[1]

    return book


#===============================UNIT TEST==============================

if __name__ == '__main__':
    # The test code below will print a list containing all books in
    # database that has an author containing a 'g' in their name.
    TEST_VALUE = db_get_books("g", 2)
    print(TEST_VALUE)
