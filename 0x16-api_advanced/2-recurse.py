#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests


def recurse(subreddit, hot_list=[], after=None, max_pages=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit (str): subreddit to query
        hot_list (list): list of hot articles
        after (str): identifier for the next page
        max_pages (int): maximum number of pages to fetch

    Returns:
        list: list of hot articles
    """
    if max_pages is not None and max_pages <= 0:
        return hot_list  # Base case: Stop when max_pages is reached or None

    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after} if after else {}

    request = requests.get(
        base_url,
        params=params,
        headers={'User-Agent': 'Agent Uche'},
        allow_redirects=False
    )

    if request.status_code != 200:
        return None  # Base case: Stop if the request fails

    data = request.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        hot_list.append(post['data']['title'])

    next_page = data.get('data', {}).get('after')
    if next_page:
        # Recursively call to fetch the next page
        return recurse(
            subreddit, hot_list, after=next_page, max_pages=max_pages
        )

    return hot_list if len(hot_list) > 0 else None
