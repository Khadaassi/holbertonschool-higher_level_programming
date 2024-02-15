#!/usr/bin/python3

""" Module for is_same_class method"""


def is_same_class(obj, a_class):
    """returns True if object is exactly an instance of the specified class;
    otherwise False."""
    return type(obj) is a_class
