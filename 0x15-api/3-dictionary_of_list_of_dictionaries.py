#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""


if __name__ == '__main__':
    import requests
    import json

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()

    todo_all_employees = {}

    for user in users:
        todos = requests.get(
                "https://jsonplaceholder.typicode.com/todos?userId={}"
                .format(user["id"]))
        todos = todos.json()

        total_tasks = []
        for todo in todos:
            del todo["id"]
            del todo["userId"]
            todo["username"] = user["username"]
            todo["task"] = todo.pop("title")
            total_tasks.append(todo)

        todo_all_employees[user["id"]] = total_tasks

    # export to JSON
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_all_employees, jsonfile)
