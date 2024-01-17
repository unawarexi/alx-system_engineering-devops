#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests


def top_ten(subreddit: str) -> None:
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts

    Args:
        subreddit (str): subreddit to query

    Returns:
        None
    """
    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    request = requests.get(
        base_url, headers={'User-Agent': 'Agent Uche'}, allow_redirects=False
    )
    data = request.json()
    try:
        for i in range(10):
            print(data['data']['children'][i]['data']['title'])
    except Exception:
        print('None')
