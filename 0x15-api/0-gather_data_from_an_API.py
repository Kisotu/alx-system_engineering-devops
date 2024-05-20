#!/usr/bin/python3
"""Task 0 - gather data from API"""

from requests import get
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    todo_url = url + "/user/{}/todos".format(argv[1])
    name_url = url + "/users/{}".format(argv[1])
    data = get(todo_url).json()
    name_result = get(name_url).json()

    todo_count = len(data)
    todo_complete = len([todo for todo in data
                         if todo.get("completed")])
    name = name_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todo_complete, todo_count))
    for todo in data:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
