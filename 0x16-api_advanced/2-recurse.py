#!/usr/bin/python3
'''Gets the top 10 hot posts for a given subreddit'''
import requests


def top_hot_subreddit(subreddit, hot_list=[], count=0, after=None):
    '''Get the top 10 hot posts for a given subreddit'''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?\
limit=100&after={after}&count={count}"

    headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64;\
rv:60.0) Gecko/20100101 Firefox/81.0"
            }

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        return None

    res = req.json().get('data')
    after = res.get('after')
    count += res.get('dist')
    titles = res.get('children')
    for title in titles:
        hot_list.append(title.get('data').get('title'))

    if after:
        top_hot_subreddit(subreddit, hot_list, count, after)

    return hot_list


def recurse(subreddit, hot_list=[]):
    '''Get the top 10 hot posts for a given subreddit'''
    return top_hot_subreddit(subreddit, hot_list, count=0, after=None)
