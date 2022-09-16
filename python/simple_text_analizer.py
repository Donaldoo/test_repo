#!/usr/bin/python3
def word_count(text):
    new_list = []
    new_list = text.split(" ")
    new_dict = {}

    for word in new_list:
        if word not in new_dict:
            new_dict[word] = 1
        else:
            new_dict[word] += 1
    return new_dict

text = "Hello this is a string Hello string dict"
print(word_count(text))
