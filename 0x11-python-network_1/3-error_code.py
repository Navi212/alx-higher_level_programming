#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8)
"""


import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            req_response = response.read()
            print(req_response.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
