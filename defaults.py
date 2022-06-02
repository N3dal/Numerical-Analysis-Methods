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
