'''Prints the inputted lists in a table format'''

import sys

def print_columns(table_name:str,
                  list1:list,
                  list2:list,
                  count:int | None = "") -> None:
    """
    Tabulates and prints a list:
    * table_name: The name of the table (Displayed above table)
    * list1: The row headings (Length determines number of columns)
    * list2: The objects to list
    * count (Default ""): Tracks position in table (Omitting disable)
                          Setting to integer determines first value
    """
    make_bold = "\033[1m"  # Start Bold string
    underline = "\033[4m"  # Start Underline
    stop = "\033[0m"  # Stop format
    num_columns = len(list1)
    space = len(str(len(list2)))  # Get space of numbering
    if count:
        format_2 = "{:2d}"  # Format numbering

    # Determine ratio of column widths by taking the maximum width per column
    ratio_list1 = [len(str(ele)) for ele in list1]
    ratio_list2 = []

    temp = []
    for i in range(0, num_columns):
        for sub_list in list2:
            try:
                temp.append(len(str(sub_list[i])))
            except IndexError:
                temp.append(0)

        ratio_list2.append(max(temp))
        temp.clear()

    ratio = []
    for i, value in enumerate(ratio_list1, 0):
        if value >= ratio_list2[i]:
            ratio.append(value)
        else:
            ratio.append(ratio_list2[i])

    # Print first line (To close table at top)
    print(make_bold, underline)
    # + 14 accounts for dividers and spaces between columns
    num = 14 if count else 9
    print(table_name, "." * (sum(ratio) + num - len(table_name)))
    if count:
        print("|   ", end=" ")

    # Print Headers (1st row)
    for i in range(num_columns):
        offset = ratio[i] + space
        print("|",f"{list1[i]:<{offset}}", end="")
    print("|")
    print(stop)

    # Print body (Remaining rows)
    sys.stdout.write('\x1b[1A' )    # Move cursor up.
    sys.stdout.write('\x1b[2K' )    # Erase line at cursor.
    print(underline)
    sys.stdout.write('\x1b[1A' )    # Move cursor up.
    sys.stdout.write('\x1b[2K' )    # Erase line at cursor.

    for ele in list2:
        # Format line 1 of each row.
        # Calculate space between elements of row 1
        if count:
            print("|", format_2.format(count), end=" ")
        for i in range(num_columns):
            offset = ratio[i] + space
            try:
                print("|",f"{ele[i]:<{offset}}", end="")
            except IndexError:
                print("|", end="")
        print("|")
        if count:
            count += 1
    print(stop)


# Call function to test functionality.
if __name__ == '__main__':  # Will only call if ran from module
    print_columns("Table: Testing the 'print_column' function",
                  ["column A", "column B", "column C"],
                  [[1, 2, 3],
                   ["a", "b", "c"],
                   ["Cats", "and","lemonade That is good... very good"]])
