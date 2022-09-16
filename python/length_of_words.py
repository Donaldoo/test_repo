#!/usr/bin/python3
def len_of_words(list):
    new_list = []
    for words in list:
        new_list.append(len(words))
    return new_list

words = ['tissue', 'psychology', 'blind', 'assessment', 'dynamic', 'hero', 'circulation', 'merchant', 'publication', 'interference', 'show', 'joy', 'sour', 'aloof', 'grass', 'distortion', 'exclude', 'pressure', 'bullet', 'calf']

print(len_of_words(words))
