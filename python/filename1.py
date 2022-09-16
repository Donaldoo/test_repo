#!/usr/bin/python3
import csv

with open('users.csv', newline='') as csvfile:
    name_to_email = {}
    reader = csv.DictReader(csvfile)
    for row in reader:
        name_to_email[row['name']] = row['email']
    email_to_name = {value: key for key, value in name_to_email.items()}
    name = email_to_name["jordan.castro@example.com"]
    print(name)
