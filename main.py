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

# for post in subreddit_stocks.hot(limit=5):
    # print('\n',post.title,'\n','##########################','\n')
    # submission = reddit.submission(post.id)
    # print top 2 comments per title submission
    # counter = 0
    # for comment in submission.comments:
        # print('COMMENT: ',comment.body,'\n')
        # counter+=1
        # if counter == 2:
            # break

def get_titles_and_comments(subreddit="stocks",limit=6,num_comments=5,skip_first=2):
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
        # Dictionary example --->>>
        # {0: "Title: Post Title \n\n Comments: \n\n"}
        title_and_comments[counter] +='Title: '+title+"\n\n"
        title_and_comments[counter] += "Comments: \n\n"

        comment_counter = 0
        for comment in submission.comments:
            if not comment.body == "[deleted]":
                title_and_comments[counter] += comment.body+"\n"
                comment_counter += 1
            if comment_counter == num_comments:
                break
    
    return title_and_comments

titles_and_comments = get_titles_and_comments()
# print("\n\n",": ) : ) : )","\n\n",titles_and_comments)

def create_prompt(title_and_comments):
    task = "Return the stock ticker or company name mentioned in following title and comments and classify the sentiment around the company as positive, negative, or neutral. If no ticker or company is mentioned write 'No Company Mentioned'\n\n"
    return task+title_and_comments

# print(titles_and_comments[1])
# print(create_prompt(titles_and_comments[1]))

for key, title_with_comments in titles_and_comments.items():

    prompt = create_prompt(title_with_comments)

    response = openai.Completion.create(engine='text-davinci-003',
                                        prompt=prompt,
                                        max_tokens=256,
                                        temperature=0,
                                        top_p=1.0
                                        )

    print("Below is the title and comments: \n\n",title_with_comments)
    print(f"Sentiment Report from OpenAI: {response['choices'][0]['text']}")
    print('-------------------------------------------')

    

































