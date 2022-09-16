#!/usr/bin/python3
import csv

with open('restaurants.csv', encoding = "ISO-8859-1") as csvfile:
    freq_table = {}
    reader = csv.DictReader(csvfile)
    for row in reader:
        kitchen = row['Cuisine']
        if kitchen in freq_table:
            freq_table[kitchen] +=  1
        else:
            freq_table[kitchen] = 1
    most_restaurants = list(sorted(freq_table.items(), key=lambda item: item[1]))[-1]

    print(freq_table)
    print(most_restaurants)
