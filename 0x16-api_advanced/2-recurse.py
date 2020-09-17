#!/usr/bin/python3
"""[summary]"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """[summary]"""
    if subreddit is None or type(subreddit) is not str:
        print(None)
    query_sub = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.
                             format(subreddit, after),
                             headers={'user-agent': 'fake_user_agent'},
                             allow_redirects=False).json()
    after = query_sub.get('data', {}).get('after', None)
    hot_children = query_sub.get('data', {}).get('children', [])
    if hot_children is None:
        if len(hot_children) == 0:
            return None
        return hot_list
    else:
        for titles in hot_children:
            hot_list.append(titles.get('data').get('title'))
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
