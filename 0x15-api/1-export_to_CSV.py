#!/usr/bin/python3
"""Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress."""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    USER_ID = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        USER_ID)).json()
    list_to_do = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            USER_ID)).json()

    with open('{}.csv'.format(USER_ID), mode='w') as file:
        user_file = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in list_to_do:
            user_file.writerow([int(USER_ID), user.get('username'),
                            task.get('completed'), task.get('title')])
