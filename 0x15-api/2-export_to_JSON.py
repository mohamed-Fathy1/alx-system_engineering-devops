#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""


if __name__ == '__main__':
    import requests
    import json
    from sys import argv

    employee_ID = argv[1]
    req = requests.get("https://jsonplaceholder.typicode.com/todos",
                       params={"userId": employee_ID})

    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(employee_ID))

    employee = employee.json()

    todos = req.json()

    for todo in todos:
        del todo["id"]
        del todo["userId"]
        todo["username"] = employee["username"]

    # export to JSON
    employee_dict = {}
    employee_dict[employee_ID] = todos

    with open("{}.json".format(employee_ID), "w") as jsonfile:
        json.dump(employee_dict, jsonfile)
