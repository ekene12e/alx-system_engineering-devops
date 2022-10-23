#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    name = user.get('name')
    totalTask = 0
    completedTask = 0

    for todo in todos:
        if todo.get('userId') == int(userId):
            totalTask += 1
            if todo.get('completed'):
                completedTask += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(name, completedTask, totalTask))
    for todo in todos:
        if todo.get('userId') == int(userId) and todo.get('completed'):
            print(f'\t {todo.get("title")}')
