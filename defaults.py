#!/usr/bin/python3


from os import name as OS_NAME
from os import system


def clear():
    """wipe terminal screen."""

    if OS_NAME == "posix":
        # for *nix machines.
        system("clear")

    else:
        # for windows machines.
        system("cls")


def approximate_error(current_approx: float, past_approx: float):
    """calculate approximate error value."""

    return abs(current_approx-past_approx)/current_approx


def true_error(true_value: float, approx_value: float):
    """calculate true error value."""

    return abs(true_value - approx_value)


def true_relative_error(true_value: float, approx_value: float):
    """calculate true relative error value."""

    return true_error(true_value, approx_value) / true_value

# we only use those chars to build the table.
# '+', '-', '|', '=', and we can use nice,
# unicode chars like that i use in xo game.


def create_table_row(data: tuple, max_length: int = None):
    """create a cli table using ascii characters."""

    COLUMNS = len(data)

    # now will find the word that have the max length of characters.
    # we will use the max length to center all the header titles strings.
    # and remember to add shifting/space value to get some space.
    SPACE_VALUE = 4

    # make sure to convert all data to string.
    data = tuple(str(element) for element in data)

    if not max_length:
        # and make sure to add space_value to avoid any bugs.
        MAX_LENGTH = len(max(data, key=lambda a: len(a))) + SPACE_VALUE
    else:
        MAX_LENGTH = max_length

    data_separate_line = ("+" + "-"*MAX_LENGTH) * COLUMNS + "+\n"

    row_data = "|" + "|".join(str(cell_data)[:MAX_LENGTH].center(MAX_LENGTH)
                              for cell_data in data) + "|\n"

    return data_separate_line + row_data + data_separate_line


data = "a", "bfdafgdafdafadfda", "c", "d"
print(create_table_row(data, max_length=10), end="")
data = 1, 2, 3, 4
# print()
