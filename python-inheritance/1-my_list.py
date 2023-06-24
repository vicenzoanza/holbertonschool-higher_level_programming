#!/usr/bin/python3
""" task 1 """
class MyList(list):
    """ prints the list, but sorted """
    def print_sorted(self):
        print(sorted(self))

