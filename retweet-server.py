import os
import tweepy
from flask import Flask
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment
from retweet_settings import *

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

@app.route('/retweet/<int:tweet_id>')
@payment.required(PRICE)
def retweet(tweet_id):
    
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    res = api.retweet(tweet_id)
    screen_name = res.author.screen_name

    return "Successfully retweeted by https://twitter.com/%s" % screen_name

if __name__ == '__main__':
    zt_ip = os.popen('ifconfig zt0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1').read().strip()
    print("-----")
    print("Server starting, to purchase a retweet from any 21BC1 use:")
    print("21 buy --maxprice {price} url http://{ip}:{port}/retweet/TWEETID".format(
        price = PRICE,
        ip = zt_ip,
        port = SERVER_PORT
    ))
    print("-----")
    app.run(host=zt_ip, port=SERVER_PORT)
