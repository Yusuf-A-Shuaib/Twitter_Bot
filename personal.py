from safe.authenticator import api


def follow_user(username:str):
    api.create_friendship(username)


def follow_users(*usernames:str):
    for username in usernames:
        api.create_friendship(username)




def tweet(message:str, image_path=None):
    if image_path:
        api.update_status(message, image_path)
    else:
        api.update_status(message)



def get_followers(username:str):
    followers = dict()
    user = api.get_user(username)

    num = 0
    for follower in user.followers():
        followers[f"Follower {num}"] = follower.name
        num+=1 

    return followers



def like_home_timeline_tweets(limit=10):
    all_tweets = api.home_timeline(count=limit)
    for tweet in all_tweets:
        if tweet.author.name.lower() != "username":
            if not tweet.favorited:
                print(f"Liking Tweet {tweet.id} from {tweet.author.name}")
                api.create_favorite(tweet.id)
                return 1
            
    



def like_user_Tweets(username:str, limit=10):
    user = api.get_user(screen_name=username)
    tweets_user = api.user_timeline(user_id=user.id, count=limit)
    for tweet in tweets_user:
        if not tweet.favorited:
            api.create_favorite(tweet.id)
            
