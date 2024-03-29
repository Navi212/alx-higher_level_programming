#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        req_response = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(req_response)))
        print("\t- content: {}".format(req_response))
        print("\t- utf8 content: {}".format(req_response.decode("utf-8")))
