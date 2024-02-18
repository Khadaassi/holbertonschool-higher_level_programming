#!/usr/bin/python3

"""
return the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """function to return the JSON representation of my_obj

        Args:
            my_obj: the object
        Returns:
            the JSON representation of my_obj
    """
    return json.dumps(my_obj)
