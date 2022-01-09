#!/usr/bin/python3

"""
    A python script that fetches https://intranet.hbtn.io/status
"""

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        output = response.read()
        print('Body response:')
        print('    - type: {}'.format(type(output)))
        print('    - content: {}'.format(output))
        print('    - utf8 content: {}'.format(output.decode('utf-8')))
