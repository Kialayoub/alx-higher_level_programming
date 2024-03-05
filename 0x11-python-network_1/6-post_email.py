#!/usr/bin/python3
"""
displays the body of the
response (decoded in utf-8) using requests
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    displays the body of the
    response (decoded in utf-8) using requests
    """
    url = argv[1]
    r = requests.post(url, data={'email': argv[2]})
    print(r.text)
