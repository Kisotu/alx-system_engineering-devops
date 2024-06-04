#!/usr/bin/python3
"""Task 1 - Top ten"""


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit"""

    from requests import get

    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)

    headers = {'user-agent': 'my-app/0.0.1'}

    req = get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        print(None)
        return None

    try:
        jsn = req.json()

    except ValueError:
        print(None)
        return None

    try:
        data = jsn.get("data")
        children = data.get("children")

        for child in children[:10]:
            post = child.get("data")
            print(post.get("title"))

    except Exception as e:
        print(None)
