#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers
for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number of
    subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data.get('data').get('subscribers')
    else:
        return 0

if __name__ == '__main__':
    print(number_of_subscribers('sex'))