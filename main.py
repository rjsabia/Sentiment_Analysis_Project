import os
import openai
import praw


openai.api_key = os.getenv('OPEN_AI_KEY_01')
# REDDIT Application ID and SECRET -- set as ENV
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID_01')
REDDIT_SECRET = os.getenv('REDDIT_SECRET_01')

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_SECRET,
                     user_agent = "sentiment analysis test"
                     )

for submission in reddit.subreddit("finance").hot(limit=5):
    print(submission.title)








