# 21-retweet

Sell retweets on Twitter using the 21 Bitcoin Computer.

## Example

You can see an example of this in action on [Twitter @21_retweet](https://twitter.com/21_retweet).
To purchase a retweet on your 21BC use:

*To use the example your 21BC1 must be connected the [21 Network](https://21.co/learn/introduction-to-the-21-bitcoin-computer/#join-the-peer-to-peer-network)*
```
21 buy --maxprice 1000 url http://21.justinguy.com/retweet/TWEETID
```

## Prerequisites

- [21 Bitcoin Computer](https://21.co)
  - Flask (`sudo pip3 install flask`)
  - Connected to the [21 Network](https://21.co/learn/introduction-to-the-21-bitcoin-computer/#join-the-peer-to-peer-network)

## First setup of server (on the 21BC)

    cd ~
    sudo pip3 install tweepy
    git clone https://github.com/justinguy/21-retweet.git
    cd 21-retweet
    cp retweet_settings_default.py retweet_settings.py

## Credentials from Twitter

In order for the Tweepy library to interact with Twitter you need API access:

- Go to https://apps.twitter.com/app/new
  - Data doesn't really matter because you will be the only consumer of the App.
- Once created click the tab "Key and Access Tokens"
- Click the button at bottom of the page "Create my access token"
- Open the `retweet_settings.py` on your 21BC
- Copy the following from Twitter -> `retweet_settings.py`
  - Consumer Key (API Key) -> `TWITTER_CONSUMER_KEY`
  - Consumer Secret (API Secret) -> `TWITTER_CONSUMER_SECRET`
  - Access Token -> `TWITTER_ACCESS_TOKEN`
  - Access Token Secret -> `TWITTER_ACCESS_TOKEN_SECRET`

## Starting the Server

    python3 retweet-server.py
    
## Purchasing Retweets

When you start the server it will provide instructions for purchasing retweets from it. This is an example:
```
-----
Server starting, to purchase a retweet from any 21BC1 use:
21 buy --maxprice 1000 url http://10.154.174.52:5000/retweet/TWEETID
-----
 * Running on http://10.154.174.52:5000/ (Press CTRL+C to quit)
```

# Todo

If you would like to improve on this here are some suggestions:
- [ ] Error handling
  - Needs to handle network errors, Twitter API errors (like rate limiting), etc
- [ ] Endpoint for server details
  - Would be nice to have an API endpoint like `/details` that returns some basic information about the retweet server such as what Twitter account is being used and maybe how many followers it has.
