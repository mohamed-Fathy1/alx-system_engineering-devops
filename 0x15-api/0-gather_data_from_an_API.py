#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""


if __name__ == '__main__':
    import requests
    from sys import argv

    employee_ID = argv[1]
    req = requests.get("https://jsonplaceholder.typicode.com/todos",
                       params={"userId": employee_ID})

    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(employee_ID))

    employee = employee.json()

    todos = req.json()
    completed_todos = []

    for todo in todos:
        if todo["completed"]:
            completed_todos.append(todo["title"])

    print("Employee {} is done with tasks({}/{}):"
          .format(employee['name'], len(completed_todos), len(todos)))
    for completed in completed_todos:
        print(f"\t {completed}")
