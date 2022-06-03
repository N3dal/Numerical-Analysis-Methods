#!/usr/bin/python3

from defaults import clear


# wipe terminal.
clear()


def math_eval(function: str, main_variable: str = "x"):
    """return a value from math equation,
    using eval and make sure that the math-equation,
    is correct."""

    # guard conditions.
    if not function:
        return None

    # now make sure to lower the function case.
    function = function.lower()

    return lambda value: eval(function.replace(main_variable, value))


def bisection(function: str, tolerance: float = 1.e-10, xl: float = 1.0, xu: float = 2.0, nmax: int = 100):
    """"""

    # initialization first.
    iter_count = 0
    error = 1.0

    while (iter_count <= nmax and error >= tolerance):

        iter_count += 1
