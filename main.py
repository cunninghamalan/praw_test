import praw


USER_AGENT="unix:prawtest:0.1 (by /u/ResponsibleOpening2)"


def main():
    client_id = None
    secret = None

    with open('client_id', 'r') as client_id_file:
        client_id = client_id_file.read().strip()

    with open('secret', 'r') as secret_file:
        secret = secret_file.read().strip()

    reddit = praw.Reddit(client_id=client_id, user_agent=USER_AGENT, client_secret=secret)
    subreddit = reddit.subreddit("learnpython")

    for submission in subreddit.hot(limit=1):
        print(submission.title)
        print(submission.selftext)
        print(submission.score)


if __name__ == "__main__":
    main()
