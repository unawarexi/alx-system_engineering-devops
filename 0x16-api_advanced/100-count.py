#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively queries the Reddit API, parses the titles of hot articles, and
    counts the occurrences of specified keywords. Prints the results in
    descending order by count, and if counts are the same, in ascending order
    by keyword.

    Args:
        subreddit (str): subreddit to query
        word_list (list): list of keywords to count
        after (str): identifier for the next page
        counts (dict): dictionary to store word counts

    Returns:
        None
    """
    if after is None:
        base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        base_url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after
        )

    headers = {'User-Agent': 'Agent Uche'}
    params = {'after': after} if after else {}

    response = requests.get(
        base_url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        title = post['data']['title'].lower()
        for keyword in word_list:
            keyword = keyword.lower()
            if (
                keyword in title
                and not title.startswith(keyword + '.')
                and not title.startswith(keyword + '!')
                and not title.startswith(keyword + '_')
            ):
                counts[keyword] = counts.get(keyword, 0) + 1

    next_page = data.get('data', {}).get('after')
    if next_page:
        count_words(subreddit, word_list, after=next_page, counts=counts)
    else:
        sorted_counts = sorted(
            counts.items(), key=lambda item: (-item[1], item[0])
        )
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
