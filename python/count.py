#!/usr/bin/python3
def count_all(list, element):
    count = 0
    for i in list:
        if i == element:
            count += 1
    return count

print(count_all([2, 2, 2, 1, 2, 1, 0, 0, 0, 2], 99))
print(count_all([2, 2, 2, 1, 2, 1, 0, 0, 0, 2], 1))
