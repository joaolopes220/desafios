# Desafio 2: Crawlers

## Parte 1
For the first part of the challenge, I created two python scripts that will virtually perform the same operation using
different methods to get the data from reddit.

### Request1.py
This version just uses request and uses a json reader to read the data.  All the information is collected this way then
displayed in the commend line.

### Praw1.py
Praw stands for Python Reddit Api Wrapper.  This version uses this wrapper to easily obtain all the data needed from
reddit.  However, to use this you need to have an account in reddit and provide some credentials for the account.  I
used this with my account and the script has this information to allow whoever runs this to have access to this api.


## Parte 2

For the second part of the challenge run the script bot1.py before running the telegram app.  If the script is running,
go in the telegram app and type tial1bot and a bot name Trial1 should pop up.  If the script is running and you select
the bot, you can now send commands to it.  If you type /NadaPraFazer [subreddits separated by ';'] [number of threads]
the bot will respond with information about the given subreddit, with the number of threads you specified.