#!/usr/bin/python3
#!/usr/bin/python3
"""Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress in JSON."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    USER_ID = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        USER_ID)).json()
    list_to_do = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            USER_ID)).json()

dict_task = []
for task in list_to_do:
    task_field = {}
    task_field['task'] = task.get('title')
    task_field['completed'] = task.get('completed')
    task_field['username'] = user.get('username')
    dict_task.append(task_field)

task_json = {}
task_json[USER_ID] = dict_task
with open('{}.json'.format(USER_ID), 'w') as file:
    json.dump(task_json, file)
