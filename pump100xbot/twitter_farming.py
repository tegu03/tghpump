# twitter_farming.py

import tweepy
import random
import time
from config import *
from utils import log_action

def get_api():
    auth = tweepy.OAuth1UserHandler(
        TWITTER_API_KEY,
        TWITTER_API_SECRET,
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_SECRET
    )
    return tweepy.API(auth)

def farming_loop():
    api = get_api()
    moonshot_accounts = [
        "moonshot_dot_so", "jup_ag", "wenwencoin", "bong0x",
        "POPCATCOIN_SOL", "0xGUMI", "moonshot_raid"
    ]
    
    tweet_phrases = [
        "I sold everything for $WEN 😤",
        "$BONG to $100M or rug, no in between 💀",
        "Farming reputation like a lunatic 💎",
        "Moonshot ecosystem only goes up 🚀",
        "Reputation > $JUP, don't @ me",
        "$POPCAT is more stable than my life 😹",
        "Degen sleep = reputation loss 😈",
        "No VC, no utility, just vibes. $GUMI 🧙",
    ]

    while True:
        try:
            # Retweet + Like 2 akun random
            for _ in range(2):
                acc = random.choice(moonshot_accounts)
                tweets = api.user_timeline(screen_name=acc, count=2)
                for tweet in tweets:
                    try:
                        if not tweet.favorited:
                            api.create_favorite(tweet.id)
                            log_action(f"LIKE | @{acc} - {tweet.id}")
                        if not tweet.retweeted:
                            api.retweet(tweet.id)
                            log_action(f"RT | @{acc} - {tweet.id}")
                        break
                    except:
                        continue

            # Chance to tweet 2–4x per hari
            if random.random() < 0.25:
                tweet = random.choice(tweet_phrases)
                api.update_status(tweet)
                log_action(f"TWEET | {tweet}")
                print(f"🐤 Tweeted: {tweet}")

            sleep_time = random.randint(1800, 3600)  # Delay 30–60 menit
            print(f"⏳ Sleeping for {sleep_time//60} minutes...")
            time.sleep(sleep_time)

        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    farming_loop()

