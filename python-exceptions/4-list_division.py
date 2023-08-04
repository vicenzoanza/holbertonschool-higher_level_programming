#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except (IndexError, ZeroDivisionError):
            print("out of range" if i >= min(len(my_list_1), len(my_list_2)) else "division by 0")
            result.append(0)
        except:
            print("wrong type")
            result.append(0)
    return result
