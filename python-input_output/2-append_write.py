#!/usr/bin/python3

"""
append a string at the end of a file
"""


def append_write(filename="", text=""):
    """function for append the text at the end of the file

        Args:
            filename: the name of the file
            text: the text to append
        Returns:
            the length of the text
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
