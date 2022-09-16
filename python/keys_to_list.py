#!/usr/bin/python3
def keys_to_list(dict):
    my_list = list(dict.keys())
    return my_list

people = {"Katherine Freeman": "katherine.freeman@hoffman.net","Tammy Gonzalez": "tammy.gonzalez@gomez.info","Robin Matthews": "robin.matthews@leblanc-lyons.org","Sherry Farrell": "sherry.farrell@reynolds-johnson.net","Emma Graves": "emma.graves@reid-little.info","Tina Brown": "tina.brown@yahoo.com","George Owens": "george.owens@yahoo.com","Ronald Ball": "ronald.ball@thomas.com"}

print(keys_to_list(people))
