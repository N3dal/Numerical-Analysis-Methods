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
