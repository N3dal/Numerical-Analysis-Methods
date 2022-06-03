#!/usr/bin/python3

from defaults import clear


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

    function.replace("^", "**")

    return lambda value: eval(function.replace(main_variable, str(value)))


def bisection(function: str, tolerance: float = 1.e-10, xl: float = 1.0, xu: float = 2.0, nmax: int = 100):
    """"""

    # initialization first.
    iter_count = 0
    error = 1.0

    while (iter_count <= nmax and error >= tolerance):

        iter_count += 1


def main():

    # wipe terminal.
    clear()

    f = math_eval("8-12*23- 2* -7")

    if f is None:
        print("Error")

    else:
        print(f(3))


if __name__ == "__main__":
    main()
