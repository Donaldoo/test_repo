#!/usr/bin/python3
def multiples_of_5(list):
    new_list = []
    for number in list:
        if number % 5 == 0:
            new_list.append(number)
    return new_list

def mult_five(list):
    return [x if x % 5 == 0 else 0 for x in list]


print(mult_five([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
