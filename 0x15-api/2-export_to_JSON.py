#!/usr/bin/python3
"""
Module 0-gather_data_from_an_API
"""

import json
import requests
from sys import argv

if __name__ == '__main__':

    id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        id)).json()
    username = user.get('username')
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(id)).json()
    json_filename = id + ".json"

    tasks = []

    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)

    dictionary = {}
    dictionary[id] = tasks

    with open(json_filename, "w") as json_file:
        json.dump(dictionary, json_file)
