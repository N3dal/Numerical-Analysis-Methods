#!/usr/bin/python3

from defaults import clear


# wipe terminal.
clear()


def bisection(function: str, tolerance: float = 1.e-10, xl: float = 1.0, xu: float = 2.0, nmax: int = 100):
    """"""

    # initialization first.
    iter_count = 0
    error = 1.0

    while (iter_count <= nmax and error >= tolerance):

        iter_count += 1

        
