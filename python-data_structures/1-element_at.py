#!/usr/bin/python3

def element_at(my_list, idx):

    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        return my_list[idx]
