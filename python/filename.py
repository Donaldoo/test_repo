#!/usr/bin/python3
import csv

with open('users.csv', newline='') as csvfile:
    name_to_email = {}
    reader = csv.DictReader(csvfile)
    for row in reader:
        name_to_email[row['name']] = row['email']
    emilia_email = name_to_email['Ms Emilia Vega']
    jordan_email = name_to_email['Mr Jordan Castro']
    print(emilia_email)
    print(jordan_email)
