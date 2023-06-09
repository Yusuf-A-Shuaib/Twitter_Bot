from safe.authenticator import api, tweepy


def Search(Keyword, limit=10):
    tweets = tweepy.Cursor(api.search, q=Keyword, lang="en").items(limit)
    for tweet in tweets:
        print(tweet)