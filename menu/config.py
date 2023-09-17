"""This module defines all constants that are used in the program"""

PROGRAM_NAME = "Hyperion Book program"
# symbols that a user may not input when updating or creating a book.
INVALID_SYMBOLS = ["@", "*", "/", "\\", "|", "%", "$", "#"]
MIN_CHAR = 3
MAX_CHAR = 50

MAIN_MENU = f'''Welcome to {PROGRAM_NAME}. Please input an option below:
      
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit
'''