#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        pass
    else:
        for elem in my_list[::-1]:
            print(f"{elem}")