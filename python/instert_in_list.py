#!/usr/bin/python3
def insert_elem(list, elem, idx):
    new_list = list[0:idx] + [elem] + list[idx:]
    return new_list

list_1 = [1, 2, 4]
print(insert_elem(list_1, 3, 2))
