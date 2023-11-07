#!/usr/bin/python3
'''Gets the top 10 hot posts for a given subreddit'''
import requests


def top_ten(subreddit):
    '''Get the top 10 hot posts for a given subreddit'''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64;\
rv:60.0) Gecko/20100101 Firefox/81.0"
            }

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        print(None)

    for res in req.json().get('data').get('children'):
        print(res.get('data').get('title'))
