#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """A subclass of list that implements print_sorted."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
