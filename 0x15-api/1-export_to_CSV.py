#!/usr/bin/python3
"""
Module 0-gather_data_from_an_API
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':

    id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        id)
    response = requests.get(user_url)
    username = response.json().get('username')
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        id)
    todo = requests.get(todo_url).json()

    with open('{}.csv'.format(id), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in todo:
            task_status = task.get('completed')
            task_title = task.get('title')
            writer.writerow([id, username, task_status, task_title])
