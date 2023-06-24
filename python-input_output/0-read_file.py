#!/usr/bin/python3
""" task 0 """
def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
