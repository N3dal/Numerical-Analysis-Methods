#!/usr/bin/python3
"""
The bisection method is an approximation method to find the roots,
of the given equation by repeatedly dividing the interval.

This method will divide the interval until the resulting,
interval is found, which is extremely small.

bisection method work for any continuous function f(x).

all equation must equal to zero.
f(x) = 0


"""

from defaults import clear
from defaults import (approximate_error)
from defaults import create_table_row
from defaults import math_eval


def bisection(function: str, tolerance: float = 1.e-10, xl: float = 1.0, xu: float = 2.0, iteration: int = 100):
    """"""

    # first initialize header data:
    HEADER_DATA = (
        "iteration",
        "xl", "xu", "xa",
        "func(xl)", "func(xu)", "func(xa)",
        "error (%)"
    )

    # initialization second.
    iter_count = 0
    error = 1.0

    # print the equation and the upper-bound and the lower-bound.
    print("Equation:", function)
    print(f"xl = {xl}")
    print(f"xu = {xu}")
    print(f"tolerance: {tolerance}%")

    # print the header table.
    print(create_table_row(HEADER_DATA, max_length=20), end="")

    # third create our math function.
    func = math_eval(function)

    while (iter_count <= iteration and error >= tolerance):

        iter_count += 1

        # xa => x-average.
        xa = (xl+xu) / 2

        if func(xa) == 0:
            # then xa is the root.
            return xa

        if func(xl) * func(xa) < 0:
            xu = xa

        else:
            xl = xa

        error = approximate_error(xu, xl)

        t = (iter_count, xl, xu, xa, func(xl),
             func(xu), func(xa), error)

        print(create_table_row(t, max_length=20), end="")


def main():

    # wipe terminal.
    clear()

    x = bisection("x^2-x-1", xl=1, xu=2, iteration=29, tolerance=3e-3)


if __name__ == "__main__":
    main()
