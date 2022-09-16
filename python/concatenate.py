#!/usr/bin/python3
def concatenate(list_1, list_2):
    list_1.extend(list_2)
    return list_1


beginning_of_quote = ['Aus', 'dem', 'Paradies,', 'das', 'Cantor', 'uns', 'geschaffen,']
rest_of_quote = ['soll', 'uns', 'niemand', 'vertreiben', 'können.']
print(concatenate(beginning_of_quote, rest_of_quote))
