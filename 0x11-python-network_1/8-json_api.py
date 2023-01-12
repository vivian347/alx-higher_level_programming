#!/usr/bin/python3
"""takes in a letter and sends a POST request
:x
"""
if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) > 1:
        val = sys.argv[1]
    else:
        val = ""
    payload = {'q': val}
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data=payload)
    if r.headers.get('content-type') == 'application/json':
        if r.json() == {}:
            print('No result')
        else:
            print(f"[{r.json().get('id')}] {r.json().get('name')}")
    else:
        print('Not a valid JSON')
