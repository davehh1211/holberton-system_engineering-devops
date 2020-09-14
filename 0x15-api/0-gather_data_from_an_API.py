#!/usr/bin/python3
"""Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress."""
import requests
from sys import argv


if __name__ == "__main__":
    USER_ID = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        USER_ID)).json()
    list_to_do = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            USER_ID)).json()

    list_of_tasks = []
    for task in list_to_do:
        if task.get('completed') is True:
            list_of_tasks.append(task.get('title'))
    print('Employee {} is done with tasks({}/{}):'.format(
        user.get('name'), len(list_of_tasks), len(list_to_do)))
    for title in list_of_tasks:
        print('\t {}'.format(title))
