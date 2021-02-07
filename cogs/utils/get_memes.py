import json
import os
import re
from datetime import timedelta

import asyncpraw


async def get_meme():
    agent = asyncpraw.Reddit(client_id='SkHY6dCDHkjQTQ',
                        client_secret='xFNsUuhhfFqrSSrpfDOZRtpNKfLu4A',
                        user_agent='THE445GUY')

    while True:
        for setting in ('day', 'hour', 'week'):
            print(os.getcwd())
            posts = await agent.subreddit('dankmemes+memes').top(setting, limit=100)
            with open(f'{os.getcwd()}/cogs/json_files/posted.json', 'r') as f:
                posted = json.load(f)
            async for post in posts:
                if not post.stickied:
                    if post.title not in posted:
                        if (post.url.find('v.redd.it/') == -1) and not post.url.endswith('.gif'):
                            posted.append(post.title)
                            with open('cogs/json_files/posted.json', 'w') as f:
                                json.dump(posted, f)
                            yield post


UNITS = {'s': 'seconds', 'm': 'minutes', 'h': 'hours', 'd': 'days', 'w': 'weeks'}


def convert_to_seconds(s):
    return int(timedelta(**{
        UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val'))
        for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', s, flags=re.I)
    }).total_seconds())
