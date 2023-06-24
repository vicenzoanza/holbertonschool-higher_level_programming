#!/usr/bin/python3
""" task 2 """
def is_same_class(obj, a_class):
    """ Check  if the object is exactly an instance of the specified class

    obj: The object to compare
    a_class: the class to compare

    return:  True if the object is exactly an instance of the specified class if not False.
    """
    return type(obj) is a_class
