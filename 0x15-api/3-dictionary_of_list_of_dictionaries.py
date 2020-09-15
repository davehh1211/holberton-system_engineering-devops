#!/usr/bin/python3
"""Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    list_to_do = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()

    user_id = {}
    for user in users:
        id_user = user.get('id')
        user_id[id_user] = []
        user_dict = {}
        user_dict[id_user] = user.get('username')

    for task in list_to_do:
        task_field = {}
        id_user = task.get('userId')
        task_field['task'] = task.get('title')
        task_field['completed'] = task.get('completed')
        task_field['username'] = user_dict.get(id_user)
        user_id.get(id_user).append(task_field)

    with open('todo_all_employees.json', 'w') as file:
        json.dump(user_id, file)
