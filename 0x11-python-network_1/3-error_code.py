#!/usr/bin/python3
""" takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read()
            print(page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code:',e.code)
