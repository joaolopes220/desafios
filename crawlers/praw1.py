import praw
import pprint
from time import sleep


# Get subreddits to crawl from user and threads per subreddit
user_input = input("Enter subreddits you wish to get data on (ex: cats;dogs;Brazil): ")
threads = int(input("Enter the number of threads per subreddit"))
subs = user_input.split(';')

# Using my account to use Praw
reddit = praw.Reddit(client_id='0Ndj0d9E6ZUS1g',
                     client_secret='1Vc08ESqyMCk_hlCAmMCxcehGlg', password='IDwallinterview',
                     user_agent='Joao', username='joaolopes220')

# Iterate through each subreddit to get data
for item in subs:
    print("Current subreddit exploring: {}".format(item))
    print('\n')
    print("------------------------------------------------------------------------------------")

    subreddit = reddit.subreddit(item)

    # Select threads that are currently hot (could change to top or new etc..)
    hot_python = subreddit.hot(limit=threads)
    count = 1
    data_info = {}

    # Store the data in dict to display
    for submission in hot_python:
        commentslink = "https://www.reddit.com{}".format(submission.permalink)
        data_info["Thread_{}".format(count)] = {
            "Title":submission.title,
            "Upvotes":submission.ups,
            "Thread Link":submission.url,
            "Comments Link":commentslink,
            "Subreddit":"/r/{}".format(item)
        }
        count +=1

    # Display the data (could also save if needed)
    for i in range(len(data_info)):

        print("Thread {}".format(i + 1))
        pprint.pprint(data_info["Thread_{}".format(i + 1)])
        print('\n')
        print('-------------------------------------------------------------------------------')
    # If we were sending to many request, this would make sure we didn't surpass limit
    #if len(subs) > 1:
        #sleep(5)
