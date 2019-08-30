from reddit import hot_posts
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from font_source_serif_pro import SourceSerifProSemibold
from font_source_sans_pro import SourceSansProSemibold
import random
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--colour', '-c', type=str, default="red",
                    choices=["red", "black", "yellow"],
                    help="ePaper display colour")
parser.add_argument('--limit', '-l', type=int, default="10",
                    help="Number of posts to get")
parser.add_argument('--subreddit', '-s', type=str, default="all",
                    help="Subreddit to search")
args = parser.parse_args()

colour = args.colour
limit = args.limit

result = hot_posts(args.subreddit, limit)
uid = random.randint(0, limit - 1)

for r in result:
    if r['id'] == uid:
        print(r['title'])
