#!/usr/bin/env python
# encoding: utf-8
import sys
import tweepy  # https://github.com/tweepy/tweepy
import csv

# Twitter API credentials
consumer_key = "fWU3vQKFwe1vpBlHd62g99CzI"
consumer_secret = "CdgpTr0oCI0VyutUMqjyKORyerTokKcPfl242KJxcUSet3Zhf8"
access_key = "1675555622-Fl4NaSWRpcqYGC0HL9g1ZU3YgikPWGWv45sSp57"
access_secret = "VFU1Hu5xDaNaKLqcflokbXY7GIgDU0D5x4xhZjJyJAHKQ"


def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []
    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    # print(alltweets)
    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))

        # all subsequent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)
        print(alltweets)

        # update the id of the oldest tweet less one
        # oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    # write the csv
    with open('tweets.csv' ,'w') as f:
        writer = csv.writer(f)
        # writer.writerow(["id", "created_at", "text"])
        writer.writerow(["text"])


        writer.writerows(outtweets)

    pass


if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("dbader_org")
    # get_all_tweets(sys.argv[1])