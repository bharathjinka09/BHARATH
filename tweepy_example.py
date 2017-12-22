# # Add this line to the top
# from authentication import authentication
# import tweepy
# if __name__ == '__main__':
#
# 	# Get access and key from another class
# 	auth = authentication()
#
# 	consumer_key = auth.getconsumer_key()
# 	consumer_secret = auth.getconsumer_secret()
#
# 	access_token = auth.getaccess_token()
# 	access_token_secret = auth.getaccess_token_secret()
#
# 	# Authentication
# 	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# 	auth.secure = True
# 	auth.set_access_token(access_token, access_token_secret)
#
# import tweepy
#
# class TwitterStreamListener(tweepy.StreamListener):
#     """ A listener handles tweets are the received from the stream.
#         This is a basic listener that just prints received tweets to stdout.
#     """
#
#     def on_status(self, status):
#         get_tweet(status)
#             get_user_informations(status)
#
#
#
# # Twitter error list : https://dev.twitter.com/overview/api/response-codes
#     def on_error(self, status_code):
#         if status_code == 403:
#             print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
#             return False
# # Create a wrapper for the API provided by Twitter
# api = tweepy.API(auth)
# api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5, retry_errors=5)
# # Create the stream
# streamListener = TwitterStreamListener()
#
# # Add your wrapper and your listener to the stream object
# myStream = tweepy.Stream(auth=api.auth, listener=streamListener)
#
# # Optional : Filter your tweet by a Hashtag or word
# 					async : Stream will run on a new thread
# myStream.filter(track=['programming'], async=True)
#
#
# def get_user_informations(tweet):
#     print("User ID \t:" + str(tweet.user.id))
#     print("User image profil \t:" + tweet.user.profile_image_url_https)
#     print("User Name \t:" + tweet.user.name)
#     print("User URL \t:", tweet.user.url)
#     print("User profil text color \t:" + tweet.user.profile_text_color)
#     print("User background image url \t:" + tweet.user.profile_background_image_url)
#     print("User Friends count \t:" + str(tweet.user.friends_count))
#     print("User Screen name \t:" + tweet.user.screen_name)
#     print("User Verified \t:" + str(tweet.user.verified))
#     print("User Favorite count \t:" + str(tweet.user.favourites_count))
#
#     if hasattr(tweet.user, 'time_zone'):
#         print("User Time zone \t:", tweet.user.time_zone)
#         print("User UTC Offset \t:" + str(tweet.user.utc_offset))
#
#     print("User Status count \t:" + str(tweet.user.statuses_count))
#
#     print("User Description \t:", tweet.user.description)
#     print("User Follower count \t:" + str(tweet.user.followers_count))
#     print("User Created at \t:" + str(tweet.user.created_at))
#
#     def get_tweet(tweet):
#
#         print("Tweet Message : " + tweet.text)
#         print("Tweet Favorited \t:" + str(tweet.favorited))
#         print("Tweet Favorited count \t:" + str(tweet.favorite_count))
#
#         # Display sender and mentions user
#         if hasattr(tweet, 'retweeted_status'):
#             print("Tweet send by : " + tweet.retweeted_status.user.screen_name)
#             print("Original tweet ID" + tweet.retweeted_status.id_str)
#
#             for screenname in tweet.retweeted_status.entities['user_mentions']:
#                 print("Mention user: " + str(screenname['screen_name']))


import tweepy
import socket
import requests
import time
from authentication import authentication  # Consumer and access token/key


class TwitterStreamListener(tweepy.StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_status(self, status):
        get_tweet(status)
        get_user_informations(status)

    # Twitter error list : https://dev.twitter.com/overview/api/response-codes

    def on_error(self, status_code):
        if status_code == 403:
            print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
            return False


def get_tweet(tweet):
    print("Tweet Message : " + tweet.text)
    print("Tweet Favorited \t:" + str(tweet.favorited))
    print("Tweet Favorited count \t:" + str(tweet.favorite_count))

    # Display sender and mentions user
    if hasattr(tweet, 'retweeted_status'):
        print("Tweet send by : " + tweet.retweeted_status.user.screen_name)
        print("Original tweet ID" + tweet.retweeted_status.id_str)

        for screenname in tweet.retweeted_status.entities['user_mentions']:
            print("Mention user: " + str(screenname['screen_name']))


def get_user_informations(tweet):
    print("User ID \t:" + str(tweet.user.id))
    print("User image profil \t:" + tweet.user.profile_image_url_https)
    print("User Name \t:" + tweet.user.name)
    print("User URL \t:", tweet.user.url)
    print("User profil text color \t:" + tweet.user.profile_text_color)
    print("User background image url \t:" + tweet.user.profile_background_image_url)
    print("User Friends count \t:" + str(tweet.user.friends_count))
    print("User Screen name \t:" + tweet.user.screen_name)
    print("User Verified \t:" + str(tweet.user.verified))
    print("User Favorite count \t:" + str(tweet.user.favourites_count))

    if hasattr(tweet.user, 'time_zone'):
        print("User Time zone \t:", tweet.user.time_zone)
    print("User UTC Offset \t:" + str(tweet.user.utc_offset))
    print("User Status count \t:" + str(tweet.user.statuses_count))

    print("User Description \t:", tweet.user.description)
    print("User Follower count \t:" + str(tweet.user.followers_count))
    print("User Created at \t:" + str(tweet.user.created_at))


if __name__ == '__main__':
    # Get access and key from another class
    auth = authentication()

    consumer_key = auth.getconsumer_key()
    consumer_secret = auth.getconsumer_secret()

    access_token = auth.getaccess_token()
    access_token_secret = auth.getaccess_token_secret()

    # Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5,
                     retry_errors=5)

    streamListener = TwitterStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=streamListener)

    myStream.filter(track=['michael'], async=True)