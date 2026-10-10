#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited

    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        True if obj is an inherited instance of a_class, else False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
