#!/usr/bin/python3
'''Gets the top 10 hot posts for a given subreddit'''
import requests


def top_hot_subreddit(subreddit, word_list, count=0, after=None, word_dict={}):
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
        title = (title.get('data').get('title')).lower().split()
        for word in title:
            if word in word_list:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

    if after:
        top_hot_subreddit(subreddit, word_list, count, after, word_dict)

    return word_dict


def count_words(subreddit, word_list):
    '''Get the top 10 hot posts for a given subreddit'''
    word_list = [word.lower() for word in word_list]
    result = top_hot_subreddit(subreddit, word_list)
    sorted_dict = sorted(result.items(), key=lambda item: item[1],
                         reverse=True)
    for key, val in sorted_dict:
        print(f"{key}: {val}")

    return result
