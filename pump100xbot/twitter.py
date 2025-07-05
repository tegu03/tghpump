# twitter.py

import tweepy
from config import *
from utils import log_action
import random

def get_api():
    auth = tweepy.OAuth1UserHandler(
        TWITTER_API_KEY,
        TWITTER_API_SECRET,
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_SECRET
    )
    return tweepy.API(auth)

def engage_twitter(symbol=None):
    api = get_api()

    # 1. Auto Retweet dan Like akun Moonshot
    moonshot_accounts = [
        "moonshot_dot_so", "jup_ag", "wenwencoin", "bong0x",
        "POPCATCOIN_SOL", "0xGUMI", "moonshot_raid"
    ]
    for user in moonshot_accounts:
        try:
            tweets = api.user_timeline(screen_name=user, count=2)
            for tweet in tweets:
                if not tweet.favorited:
                    api.create_favorite(tweet.id)
                if not tweet.retweeted:
                    api.retweet(tweet.id)
        except Exception as e:
            print(f"❌ Gagal engage @{user}: {e}")

    # 2. Tweet absurd random
    if random.random() < 0.3:  # hanya 30% loop akan tweet
        phrases = [
            f"I sold my cat for ${symbol or 'WEN'}",
            f"{symbol or '$MOON'} > $BTC 🫡",
            f"Degen only lives once 🚀",
            f"Reputation > Capital. Farm with me. #moonshot",
            f"{symbol or '$GUMI'} is my religion now 🙏",
        ]
        tweet = random.choice(phrases)
        api.update_status(tweet)
        log_action(f"TWEET | {tweet}")
        print(f"🐤 Tweeted: {tweet}")

