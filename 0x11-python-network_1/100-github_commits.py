#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of the
repository "rails" by user "rails" you must use the githubapi
Print all commits by: <sha>: <author name>` (one by line)
"""

if __name__ == "__main__":
    import requests
    import sys
    repo = sys.argv[2] + "/" + sys.argv[1]
    url = 'https://api.github.com/repos/{0}/commits?per_page=10'.format(repo)
    r = requests.get(url)
    for info in r.json():
        sha = info.get('sha')
        name = info.get('commit').get('author').get('name')
        print('{}: {}'.format(sha, name))
