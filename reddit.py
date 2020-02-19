#!/usr/bin/env python

import sys
import os
import praw
import json
from pathlib import Path

DEFAULT_LIMIT = 1000
DEFAULT_PATH = 'data'

def fetch(client, subreddit, output_name, sort='top', limit=DEFAULT_LIMIT, replace_more=32):
        if os.path.exists(output_name):
            print(f"skipping {output_name}")
            return
        print(f"fetching {limit} {sort} from {subreddit} ...")
        docs = []
        func = getattr(client.subreddit(subreddit), sort)
        for submission in func(limit=limit):
            comments = submission.comments
            comments.replace_more(replace_more)
            comment_texts = [{
                'body': comment.body,
                'created_utc': comment.created_utc,
                'score': comment.score}
                    for comment in comments]
            sub = {
                'title': submission.title,
                'text': submission.selftext,
                'upvote_ratio': submission.upvote_ratio,
                'score': submission.score,
                'created_utc': submission.created_utc,
                'url': submission.url,
                'permalink': submission.permalink,
                'is_self': submission.is_self,
                'num_comments': submission.num_comments,
                'comments': comment_texts,
            }
            docs.append(sub)
        with open(output_name, 'w') as handle:
            json.dump(docs, handle, indent=4, ensure_ascii=False)


def load(subreddits, path=DEFAULT_PATH, sort='top'):
    data = []
    for subreddit in subreddits:
        subreddit = subreddit.strip()
        if not subreddit or subreddit.startswith('#'):
            continue
        subreddit = subreddit.rstrip('/').split('/')[-1].lower()
        data += json.load(open(f'{path}/{subreddit}_{sort}.json', 'r', encoding='utf8'))
    print(f"loaded {len(data)} reddit submissions")
    return data


def main():
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('--sort', '-s', choices=('top', 'hot', 'new', 'rising', 'controversial', 'gilded'), default='top')
    parser.add_argument('--limit', '-l', type=int, default=DEFAULT_LIMIT)
    parser.add_argument('list')
    args = parser.parse_args()

    print(f"fetching {args.limit} {args.sort} submissions")

    output_dir = Path(DEFAULT_PATH)
    output_dir.mkdir(exist_ok=True)

    client = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),
                         client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                         user_agent=os.getenv('REDDIT_USER_AGENT'))

    with open(args.list, 'r') as subreddits:
        for subreddit in subreddits:
            subreddit = subreddit.strip()
            if not subreddit or subreddit.startswith('#'):
                continue
            subreddit = subreddit.rstrip('/').split('/')[-1]
            output_name = output_dir.joinpath('{0}_{1}.json'.format(subreddit.lower(), args.sort))
            fetch(client, subreddit, output_name=output_name, sort=args.sort, limit=args.limit)


if __name__ == '__main__':
    main()
    print("done")
