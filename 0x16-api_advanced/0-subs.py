#!/usr/bin/python3
'''Gets the number of subscribers for a given subreddit'''
import requests


def number_of_subscribers(subreddit):
    '''Gets the number of subscribers for a given subreddit'''
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64;\
rv:60.0) Gecko/20100101 Firefox/81.0"
            }

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        return 0
    return req.json().get('data').get('subscribers')
