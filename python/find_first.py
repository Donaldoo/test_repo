#!/usr/bin/python3
def find_first(list, value):
    try:
        for i in range(len(list)):
            if list[i] == value:
                return i
    except:
        return -1

print(find_first([2, 2, 2, 1, 2, 1, 0, 0, 0, 2], 99))
print(find_first([2, 2, 2, 1, 2, 1, 0, 0, 0, 2], 1))
