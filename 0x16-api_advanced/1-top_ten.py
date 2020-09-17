#!/usr/bin/python3
"""[summary"""
import requests


def top_ten(subreddit):
    """
    Args:
        subreddit (query): [description]
    """
    if subreddit is None or type(subreddit) is not str:
        print(None)
    query_sub = requests.get('https://www.reddit.com/r/{}/hot.json'.
                             format(subreddit),
                             headers={'user-agent': 'fake_user_agent'},
                             allow_redirects=False).json()
    sub_number = query_sub.get('data', {}).get('children', [])
    if not sub_number:
        print(None)
    for tops in sub_number[:10]:
        print(tops.get('data').get('title'))
