#!/usr/bin/python3

"""
    Write a Python script that takes in a URL, sends a request to the URL
    and displays the body of the response.

    If the HTTP status code is greater than or equal to 400,
    print: Error code: followed by the value of the HTTP status code

    Uses the package requests
"""

import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
