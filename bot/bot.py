import tweetpy

api = tweetpy.Client(

    consumer_key='KEY',
    consumer_secret='KEY',
    access_token='KEY',
    access_token_secret='KEY'
)

try:
    tweet = api.create_tweet(text="Te odeio")
    print(tweet)
except:
    print("Deu errado")
