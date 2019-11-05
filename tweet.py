import tweepy
import time

auth = tweepy.OAuthHandler(
    "CcygYx9P8I8kSsDtZYMmohL6o", "heASpZfMW9Fnj0P3NwgeGMwoKN1t3MDrtp2yLVyvGed9HoIuxB"
)
auth.set_access_token(
    "4186603517-nwUpmz9R1zL8PFy4ZgeXrRrIzjIEaBjQ7MKu9Qy",
    "hXM3yjBKoVdQpQwOE9QLlhVmwdDSXD0o6mtVG7zyVUyAl",
)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print("-------------------------------------")
#     print(tweet.text)

user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == "Scholarships":
        print(follower.follow())
        break


search_string = "javascript"
numbersOfTweets = 2


for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.retweet()
        print(tweet.text)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
