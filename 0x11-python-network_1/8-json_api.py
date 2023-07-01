#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.

    The letter must be sent in the variable q
    If no argument is given, set q=""
    If the response body is properly JSON formatted and not empty,
    display the id and name like this: [<id>] <name>
    Otherwise:
        Display Not a valid JSON if the JSON is invalid
        Display No result if the JSON is empty
    Must use the package requests and sys
    Not allowed to import packages other than requests and sys
"""


import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]
    payload = {"q": letter}
    req = requests.post(url, data=payload)
    try:
        dit = req.json()
        if dit:
            print("({}) {}".format(dit.get("id"), dit.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
