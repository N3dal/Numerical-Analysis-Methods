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


def math_eval(function: str, main_variable: str = "x"):
    """return a math function that we can,
    evaluate.

    + => for addition.
    - => for subtraction.
    * => for multiplication.
    / => for division.
    ^ => for power.
    -x => for negative numbers.

    and you can use parentheses => '(' or ')'.

    note: you can only have only one main variable.
    note: spaces is allowed but try to avoid using them.

    valid examples:
        func(3) = 3*x+23/3^2
        func(3.3) = 8-12*23-2 * -7
        func(3.3) = 8-12*23-2*-7

    non-valid examples:
        func(3) = 3*xy23/234
        func(-1) = 12y+7 and the main-variable is x.
        func(-2) = 23&34|5!math.

        so you can't use any symbols except the symbols that,
        in ELEMENTS.


    """

    # guard conditions.
    if not function:
        return None

    # now make sure to lower the function case.
    function = function.lower()

    # and make sure to lower main variable.
    main_variable = main_variable.lower()

    # the elements that we only want to be on our function.
    ELEMENTS = (
        " ", "+", "-", "^", "/", "*", "(", ")", main_variable
    )

    if not all(element in ELEMENTS or element.isdecimal()
               for element in function):
        # if everything not ok and our function,
        # contain other symbols or other variables.
        return None

    function = function.replace("^", "**")

    return lambda value: eval(function.replace(main_variable, str(value)))


def approximate_error(current_approx: float, past_approx: float):
    """calculate approximate error value."""

    return (abs(current_approx-past_approx)/current_approx) * 100


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
