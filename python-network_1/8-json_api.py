#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': letter}
    try:
        url = 'http://0.0.0.0:5000/search_user'
        response = requests.post(url, data=payload)
        json_response = response.json()
        if json_response:
            uid = json_response.get('id')
            uname = json_response.get('name')
            print(f"[{uid}] {uname}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
