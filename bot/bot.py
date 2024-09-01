from typing import Tuple

import tweetpy

  consumer_key = 'tzQJZuseeZcmalxAlrLPpaOWf',
  consumer_secret='ox6uoHfat9B8rdxtLtyHKgVmDjejsHA19YEGNBUfh3DyPc5daE',
  access_token='1073389205915623430-oBzapCa9jPfNUCxknLwVCq7Xb1sV3P',
  access_token_secret='w4x0eI1ROBqDBbbPO7gWkhIk2HKV4H3Hb5KGhlE22HfFQ'

auth = tweetpy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweetpy.API(auth, wait_on_rate_limit=True)

def post_tweet(text):
    api.update_status(text)
