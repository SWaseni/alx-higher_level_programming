#!/usr/bin/python3
"""Read text file"""


def read_file(filename=""):
    """open file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
