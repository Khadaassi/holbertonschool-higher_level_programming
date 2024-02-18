#!/usr/bin/python3

"""read a file"""


def read_file(filename=""):
    """function for read a file"""
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.read()
        file.close()
    print(lines, end="")
