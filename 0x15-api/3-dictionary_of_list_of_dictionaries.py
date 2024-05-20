#!/usr/bin/python3
"""fetches API data and exports dictionary to JSON"""

from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    data = get(url).json()

    mydict = {}
    for user in data:
        mylist = []

        pep_fix = "https://jsonplaceholder.typicode.com"
        todos_url = pep_fix + "/user/{}/todos".format(user.get("id"))
        name_url = "https://jsonplaceholder.typicode.com/users/{}".format(
            user.get("id"))

        todo_result = get(todos_url).json()
        name_result = get(name_url).json()
        for todo in todo_result:
            todo_dict = {}
            todo_dict.update({"username": name_result.get("username"),
                              "task": todo.get("title"),
                              "completed": todo.get("completed")})
            mylist.append(todo_dict)

        mydict.update({user.get("id"): mylist})

    with open("todo_all_employees.json", 'w') as f:
        dump(mydict, f)
