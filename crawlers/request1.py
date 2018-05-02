import requests
import pprint


# Get subreddits from user to explore
# This version only obtains the threads from the first page
user_input = input('Enter subreddits you wish to explore')
subreddit = user_input.split(';')


# Iterate through subreddits for data
for sub in subreddit:
    print("Current Subreddit /r/{}".format(sub))
    # Obtain data from the website as json file
    r = requests.get(
        'http://www.reddit.com/r/{}/.json'.format(sub),
        headers={'user-agent': 'Mozilla/5.0'}
    )

    #Iterate through json to get information in the format we want
    count = 1
    final_info = {}
    for post in r.json()['data']['children']:
        link = "https://reddit.com{}".format(post['data']['permalink'])
        final_info["Thread_{}".format(count)] = {"Title": (post['data']['title']),
                                                 "Comments Link": link,
                                                 "Upvotes": (post['data']['score']),
                                                 "Subreddit": (post['data']['subreddit']),
                                                 "Thread Link": post['data']['url']
                                                 }
        count += 1

    # Displays the data
    for i in range(len(final_info)):
         print("Thread {}".format(i + 1))
         pprint.pprint(final_info["Thread_{}".format(i + 1)])
         print('\n')
         print('-------------------------------------------------------------------------------')
