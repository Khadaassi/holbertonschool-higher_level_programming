#!/usr/bin/python3

""" Module for lookup method """


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.
    Args:
        obj: object to look up
    Returns: list of available attributes and methods of an object.
    """
    return dir(obj)
