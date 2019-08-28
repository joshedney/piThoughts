import praw
import os
from dotenv import load_dotenv

# Load the variables from the .env file
load_dotenv()

# Reddit API auth
reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'),
                     client_secret=os.getenv('CLIENT_SECRET'),
                     user_agent=os.getenv('USER_AGENT'))


def get_hot_posts(subreddit, limit):
    posts = []
    n = 0
    for p in reddit.subreddit(subreddit).hot(limit=limit):
        post = {}
        post['id'] = n
        post['author'] = p.author.name
        post['title'] = p.title
        posts.append(post)
        n += 1

    return posts
