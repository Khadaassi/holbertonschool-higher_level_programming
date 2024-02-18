#!/usr/bin/python3
'''
    This module contains a class Student
'''


class Student:
    '''Initialization of attributes

            Args:
                first_name(str): first attribute
                last_name(str): second attribute
                age(int): third attribute
    '''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary
        """

        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

        return (self.__dict__)

    def reload_from_json(self, json):
        """Replaces attributes of instance"""
        for key, value in json.items():
            setattr(self, key, value)
