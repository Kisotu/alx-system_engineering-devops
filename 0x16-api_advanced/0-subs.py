#!/usr/bin/python3
"""Task 0 - how many subs"""


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""

    from requests import get

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {'user-agent': 'my-app/0.0.1'}

    req = get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        return 0

    try:
        js = req.json()

    except ValueError:
        return 0

    data = js.get("data")

    if data:
        sub_count = data.get("subscribers")
        if sub_count:
            return sub_count

    return 0
