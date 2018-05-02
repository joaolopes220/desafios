import json
import praw
import requests
import time
import urllib

#bot name is Trial1
#account is tial1bot

# The bot token and url
TOKEN = "594731133:AAE8n8J8GHIE_t6p9cSLPAn1ltSfSi1gHPg"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    """
    :param url: bot url
    :return: content from messages received
    """
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    """
    :param url: bot url
    :return: json of content
    """
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    """
    :return: json from updated messages received
    """
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    """
    :param updates: content from last message
    :return: last id
    """

    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def handle_updates(updates):
    """

    :param updates:  content from last message
    :return: None
    """
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        text_list = text.split()
        if text_list[0] == "/done":
            send_message("Goodbye", chat)
        elif text_list[0] == "/start":
            send_message("Welcome to you reddit quick info bot", chat)
        elif text_list[0] =="/NadaPraFazer":
            if len(text_list) == 3:
                crawler(text_list[1], chat, text_list[2])
            else:
                crawler(text_list[1], chat, 3)
        elif text.startswith("/"):
            continue


def get_last_chat_id_and_text(updates):
    """

    :param updates: information about the message
    :return: text from the message and id from user
    """
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return text, chat_id


def send_message(text, chat_id):
    """

    :param text: message wishing to send
    :param chat_id: id of user wishing to send message to
    :return: None
    """
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def crawler(user_input, chat, threads):
    """

    :param user_input: subreddit to get data from
    :param chat: id for user to send data too
    :param threads: number of threads per subreddit to be messaged
    :return: None
    """

    #split the different subreddits
    subs = user_input.split(';')
    # Using my account to use Praw
    reddit = praw.Reddit(client_id='0Ndj0d9E6ZUS1g',
                         client_secret='1Vc08ESqyMCk_hlCAmMCxcehGlg', password='IDwallinterview',
                         user_agent='Joao', username='joaolopes220')

    thread_count = int(threads)
    # Iterate through each subreddit to get data
    for item in subs:
        subreddit = reddit.subreddit(item)

        # Select threads that are currently hot (could change to top or new etc..)
        hot_python = subreddit.hot(limit=thread_count)
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

        # Message out the information on each thread
        for i in range(len(data_info)):
            send_message("{} Thread {}".format(item, i + 1), chat)
            send_message("Thread Title: {}".format(data_info["Thread_{}".format(i + 1)]["Title"]), chat)
            send_message("Subreddit: {}".format(data_info["Thread_{}".format(i + 1)]["Subreddit"]), chat)
            send_message("Upvotes: {}".format(data_info["Thread_{}".format(i + 1)]["Upvotes"]), chat)
            send_message("Thread Link: {}".format(data_info["Thread_{}".format(i + 1)]["Thread Link"]), chat)
            send_message("Comments Link: {}".format(data_info["Thread_{}".format(i + 1)]["Comments Link"]), chat)
            send_message('   ', chat)


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)



if __name__ == '__main__':
    main()
