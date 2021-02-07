import json

import praw
import os


def get_meme():
    agent = praw.Reddit(client_id='SkHY6dCDHkjQTQ',
                        client_secret='xFNsUuhhfFqrSSrpfDOZRtpNKfLu4A',
                        user_agent='THE445GUY')

    while True:
        for setting in ('day', 'hour', 'week'):
            print(os.getcwd())
            posts = agent.subreddit('dankmemes+memes').top(setting, limit=100)
            with open(f'{os.getcwd()}/cogs/json_files/posted.json', 'r') as f:
                posted = json.load(f)
            for post in posts:
                if not post.stickied:
                    if post.title not in posted:
                        if (post.url.find('v.redd.it/') == -1) and not post.url.endswith('.gif'):
                            posted.append(post.title)
                            with open('cogs/json_files/posted.json', 'w') as f:
                                json.dump(posted, f)
                            yield post
