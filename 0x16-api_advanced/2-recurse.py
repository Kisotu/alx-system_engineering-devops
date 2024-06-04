#!/usr/bin/python3
"""Task 2 - Recurse it!"""

from requests import get

REDDIT = "https://www.reddit.com/"
HEADERS = {'user-agent': 'my-app/0.0.1'}


def recurse(subreddit, hot_list=[], after=""):
    """
    recursive function that queries the Reddit API
    returns a list containing the titles of
    all hot articles for a given subreddit"""

    if after is None:
        return hot_list

    url = REDDIT + "r/{}/hot/.json".format(subreddit)

    params = {
        'limit': 100,
        'after': after
    }

    req = get(url, headers=HEADERS, params=params, allow_redirects=False)

    if req.status_code != 200:
        return None

    try:
        jsn = r.json()

    except ValueError:
        return None

    try:
        data = jsn.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            hot_list.append(post.get("title"))

    except Exception as e:
        return None

    return recurse(subreddit, hot_list, after)
