#!/usr/bin/python3

"""
object represented by a JSON string
"""
import json


def from_json_string(my_str):
    """function to return an object of a JSON string

        Args:
            my_str: the str
        Returns:
            the object
    """
    return json.loads(my_str)
