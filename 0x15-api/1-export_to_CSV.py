#!/usr/bin/python3
"""fetches data JSONplaceholder API and exports to CSV"""

from csv import DictWriter, QUOTE_ALL
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    todo_url = url + "/user/{}/todos".format(argv[1])
    name_url = url + "/users/{}".format(argv[1])
    data = get(todo_url).json()
    name_result = get(name_url).json()

    mylist = []
    for todo in data:
        todo_dict = {}
        todo_dict.update({"user_ID": argv[1], "username": name_result.get(
            "username"), "completed": todo.get("completed"),
                          "task": todo.get("title")})
        mylist.append(todo_dict)
    with open("{}.csv".format(argv[1]), 'w', newline='') as f:
        header = ["user_ID", "username", "completed", "task"]
        writer = DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
        writer.writerows(mylist)
