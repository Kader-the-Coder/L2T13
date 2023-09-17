"""This module is responsible for checking all user inputs."""

#=======================IMPORT LIBRARIES/MODULES=======================
# pylint: disable=import-error

from display.clear_lines import clear_lines
from config import INVALID_SYMBOLS, MIN_CHAR, MAX_CHAR

# pylint: enable=import-error
#===========================DEFINE FUNCTION============================


def input_value(message:str, is_text:bool | None = True) -> str:
    """Requests and checks user input"""
    while True:
        flag = True # To handle break in nested for loop
        user_input = input(message)
        user_input = user_input.strip()

        if user_input == "":
            print("\nYou did not input anything")
            input("Press enter to try again")
            clear_lines(4)
            continue
        # If expected user_input can be any text:
        if is_text:
            # Check if user_input is of valid length.
            if len(user_input) < MIN_CHAR or len(user_input) > MAX_CHAR:
                print("\nInvalid input. Please ensure that your input is\n"
                      f"from {MIN_CHAR} to {MAX_CHAR} characters long.")
                input("Press enter to try again")
                clear_lines(5)
                continue
            # Check if user_input does not contain any invalid symbols.
            for symbol in INVALID_SYMBOLS:
                if symbol in user_input:
                    print(f"\n\"{symbol}\" may not be used.")
                    input("Press enter to try again")
                    clear_lines(4)
                    flag = False
                    break
        else:
            # If expected user_input must be a positive integer:
            if user_input.replace(".","_").isnumeric():
                return user_input

            print("\nInvalid input. Please ensure that your input is\n"
                    "a positive integer")
            input("Press enter to try again")
            clear_lines(5)
            continue

        if flag:
            return user_input


def input_field(message:str):
    """Returns user input if it is in 'field_list'"""
    field_list = ["title", "author", "qty"]
    while True:
        temp = input(message)
        temp = temp.strip()
        temp = temp.lower()

        if temp == "":
            print("\nYou did not input anything")
            input("Press enter to try again")
            clear_lines(4)
            continue

        if temp.lower() in field_list:
            return temp
        print(f"\n\"{temp}\" is not a valid field.")
        input("Press ENTER to try again")
        clear_lines(4)


#=============================Unit Test================================

if __name__ == "__main__":
    test = input_value("field: ")
    test = input_value("value: ", False)
