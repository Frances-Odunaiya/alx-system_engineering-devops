#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(url)).json()
    todos = requests.get(url + "/todos").json()

    dict = {}
    for user in users:
        arr = []
        user_id = user.get('id')
        for todo in todos:
            if user.get('id') == todo.get('userId'):
                arr.append({'task': todo.get('title'),
                            'completed': todo.get('completed'),
                            'username': user.get('username')})
        dict[user_id] = arr

    filename = "todo_all_employees.json"
    with open(filename, "w", encoding="utf-8") as json_file:
        json_text = json.dumps(dict)
        json_file.write(json_text)
