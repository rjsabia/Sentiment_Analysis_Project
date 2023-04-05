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

# ---- running some tests on interacting with the reddit api ----
# for submission in reddit.subreddit("finance").hot(limit=5):
    # print(submission.title)  # Example for acces to category -->
                               # reddit.com/r/stocks

# for submission in reddit.subreddit("stocks").hot(limit=10):
    # print(submission.title)

subreddit_stocks = reddit.subreddit("stocks")

# ---- Example of some data points you can drill into ----
# subreddit_stocks.title
# subreddit_stocks.display_name
# subreddit_stocks.acounts_active
# etc etc tons of ways to drill in
# print('\n',subreddit_stocks.accounts_active)
# print('\n',subreddit_stocks.title)
# subreddit_stocks.accounts_active

for post in subreddit_stocks.hot(limit=5):
    print('\n',post.title,'\n','##########################','\n')
    submission = reddit.submission(post.id)
    # print top 2 comments per title submission
    counter = 0
    for comment in submission.comments:
        print('COMMENT: ',comment.body,'\n')
        counter+=1
        if counter == 2:
            break

def get_titles_and_comments(subreddit="stocks",limit=6,num_comments=3,skip_first=2):
    subreddit = reddit.subreddit(subreddit)
    title_and_comments = {}

    for counter,post in enumerate(subreddit.hot(limit=limit)):

        if counter < skip_first:
            continue

        counter += (1-skip_first)

        title_and_comments[counter] = ""
        # this is using the PRAW library again
        submission = reddit.submission(post.id)
        title = post.title

        title_and_comments[counter] +='Title: '+title+"\n\n"
        title_and_comments[counter] += "Comments: \n\n"
















