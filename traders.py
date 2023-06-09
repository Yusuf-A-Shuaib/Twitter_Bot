from safe.authenticator import api


def follow_users(*usernames:str):
    for username in usernames:
        api.create_friendship(username)



def like_user_Tweets(username:str):
    user = api.get_user(username)
    tweets_user = api.user_timeline(user_id=user.id, count=10)
    for tweet in tweets_user:
        if not tweet.favorited:
            api.create_favorite(tweet.id)




def get_latestTweet(username:str):
    user = api.get_user(username)
    for tweet in user.tweets:
        print(tweet)


def get_trader_data(username:str):
    user_data = dict()
    user = api.get_user(username)
    user_data["Name"] = user.name
    user_data["Description"] = user.description

    num = 0
    for follower in user.followers():
        user_data[f"Follower {num}"] = follower.name
        num+=1

    return user_data