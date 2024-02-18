#!/usr/bin/python3
"""
Module for task 8
"""


def class_to_json(obj):
    """ Return the dictionary represntation of a simple data structure """
    jsonObj = obj.__dict__
    return (jsonObj)
