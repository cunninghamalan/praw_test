import praw
from praw.models import MoreComments

USER_AGENT="unix:prawtest:0.1 (by /u/ResponsibleOpening2)"

def traverse_comment_depth_first(comment, depth=1):
    indent = "  " * depth
    print("{}- Comment Author: {}".format(indent, comment.author))
    print("{}  Comment Score: {}".format(indent, comment.score))
    # print("{}  Comment Text: {}".format(indent, comment.body))
    print()
    for comment in comment.replies:
        traverse_comment_depth_first(comment, depth=depth+1)
        

def parse_submission_comments(submission, more_comments_limit=None):

    # Replaces  the "Load More Comments Comments with real comments
    # Requires a web-request for each one.
    # A value of None replaces them all.
    submission.comments.replace_more(limit=more_comments_limit)
    for comment in submission.comments.list():
        traverse_comment_depth_first(comment)


def main():
    client_id = None
    secret = None

    with open('client_id', 'r') as client_id_file:
        client_id = client_id_file.read().strip()

    with open('secret', 'r') as secret_file:
        secret = secret_file.read().strip()

    reddit = praw.Reddit(client_id=client_id, user_agent=USER_AGENT, client_secret=secret)
    subreddit = reddit.subreddit("0thworldproblems")

    for submission in subreddit.top('all', limit=1000):
        print("Title: {}".format(submission.title))
        print("Score: {}".format(submission.score))
        print("Author: {}".format(submission.author))
        print("Text: {}".format(submission.selftext))
        print()

        parse_submission_comments(submission)

if __name__ == "__main__":
    main()
