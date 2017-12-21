import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "fWU3vQKFwe1vpBlHd62g99CzI",
    "consumer_secret"     : "CdgpTr0oCI0VyutUMqjyKORyerTokKcPfl242KJxcUSet3Zhf8",
    "access_token"        : "1675555622-Fl4NaSWRpcqYGC0HL9g1ZU3YgikPWGWv45sSp57",
    "access_token_secret" : "VFU1Hu5xDaNaKLqcflokbXY7GIgDU0D5x4xhZjJyJAHKQ"
    }

  api = get_api(cfg)
  tweet = "Good Night all"
  status = api.update_status(status=tweet)
  # status = api.update_with_media(image_path, tweet)
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()