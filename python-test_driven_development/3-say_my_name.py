#!/usr/bin/python3

""" Prints first and last name """


def say_my_name(first_name, last_name=""):
    """
    Prints first and last name
    Args:
        first_name (str): first name
        last_name (str, optional): last name, default to ""
    Raises:
        TypeError: if first_name is not a str
        TypeError: if last_name is not a str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
