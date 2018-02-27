import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "B4CUqhMKRxspERyZZGzv7GHpo",
    "consumer_secret"     : "1TxEinoNNJIYdUBsfi1Z31NDvRK6DiKXK0J8ZKVMQLmnqptTtH",
    "access_token"        : "853661402053083136-LBwlkvHiUFxuiaCn3vmvHLYOORfTeom",
    "access_token_secret" : "xxgN1k4EzuMeXwXT29eAvHXGkirSYtEjjWKGaHXehpPEG" 
    }

  api = get_api(cfg)
  tweet = "Python greetings :)"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
