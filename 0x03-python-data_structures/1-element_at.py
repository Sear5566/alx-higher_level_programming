#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    for elem in range(len(my_list)):
        if elem == idx:
            return my_list[elem]
