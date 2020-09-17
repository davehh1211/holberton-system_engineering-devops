#!/usr/bin/python3
"""Write a function that queries the Reddit API
and returns the number of subscribers (not active users,
total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Args:
        subreddit (query): [description]
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    query_sub = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), headers={'user-agent': 'fake_user_agent'}).json()
    sub_number = query_sub.get('data', {})
    sub_number2 = sub_number.get('subscribers', 0)
    return(sub_number2)
