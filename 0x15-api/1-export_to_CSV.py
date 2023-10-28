#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""


if __name__ == '__main__':
    import requests
    import csv
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

    # export to CSV
    with open("{}.csv".format(employee_ID), "w") as csvfile:
        write = csv.writer(csvfile, delimiter=',',
                           quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in todos:
            write.writerow([employee_ID, employee["name"],
                            todo["completed"], todo["title"]])
