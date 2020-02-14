#!/usr/bin/env python

import sys
import os
import praw
import json
from pathlib import Path

DEFAULT_LIMIT = 100
DEFAULT_PATH = 'data'

def fetch(client, subreddit, output_name, hot_or_top='top', limit=DEFAULT_LIMIT):
        if os.path.exists(output_name):
            print(f"skipping {output_name}")
            return
        print(f"fetching {subreddit} ...")
        docs = []
        func = getattr(client.subreddit(subreddit), hot_or_top)
        for submission in func(limit=limit):
            comments = submission.comments
            comments.replace_more(32)
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


def load(subreddits, path=DEFAULT_PATH, hot_or_top='top'):
    data = []
    for subreddit in subreddits:
        subreddit = subreddit.strip()
        if not subreddit or subreddit.startswith('#'):
            continue
        subreddit = subreddit.rstrip('/').split('/')[-1].lower()
        data += json.load(open(f'{path}/{subreddit}_{hot_or_top}.json', 'r', encoding='utf8'))
    print(f"loaded {len(data)} reddit submissions")
    return data


def main():
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('--type', '-t', choices=('top', 'hot'), default='top')
    parser.add_argument('--limit', '-l', type=int, default=DEFAULT_LIMIT)
    parser.add_argument('list')
    args = parser.parse_args()

    print(f"fetching {args.limit} {args.type} submissions")

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
            output_name = output_dir.joinpath('{0}_{1}.json'.format(subreddit.lower(), args.type))
            fetch(client, subreddit, output_name=output_name, hot_or_top=args.type, limit=args.limit)


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit("exiting")
    print("done")
