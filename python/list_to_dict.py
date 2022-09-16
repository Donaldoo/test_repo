#!/usr/bin/python3
def list_to_dict(list1, list2):
    new_dict = {}
    for i in range(len(list1)):
            new_dict[list1[i]] = list2[i]
    return new_dict

keys = ['Katherine Freeman', 'Tammy Gonzalez', 'Robin Matthews', 'Sherry Farrell', 'Emma Graves', 'Tina Brown', 'George Owens', 'Ronald Ball']

values = ['katherine.freeman@hoffman.net', 'tammy.gonzalez@gomez.info', 'robin.matthews@leblanc-lyons.org', 'sherry.farrell@reynolds-johnson.net', 'emma.graves@reid-little.info', 'tina.brown@yahoo.com', 'george.owens@yahoo.com', 'ronald.ball@thomas.com']
print(list_to_dict(keys, values))
