#!/usr/bin/python3

"""
write in a file
"""


def write_file(filename="", text=""):
    """function for write in a file

        Args:
            filename: the name of the file
            text: the text in the file
        Returns:
            the lenght of the text in file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
