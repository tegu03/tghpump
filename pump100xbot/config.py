# config.py
from dotenv import load_dotenv
import os

load_dotenv()

# Wallet & RPC
PRIVATE_KEY = os.getenv("WALLET_PRIVATE_KEY")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")
RPC_URL = os.getenv("RPC_URL")

# Twitter Auth
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# Trade Settings
BUY_LIMIT_SOL = 0.01
TP_MULTIPLIER = 2.0
SL_PERCENT = -25

# Screening Criteria
MIN_HOLDERS = 160
MAX_MARKETCAP = 30000
MIN_VOLUME = 10000
MIN_LIQUIDITY = 20000
MAX_CURVE = 90
MAX_TOP10_HOLDERS = 20
MAX_DEV_WALLET = 3
MIN_AGE_MINUTES = 10
MAX_AGE_MINUTES = 20

# Twitter Farming
TWITTER_USERNAME = "@zupinzin"
TWITTER_ACCOUNTS_TO_ENGAGE = [
    "pumpdotfun", "rektguyeth", "4amvc", "solportdotio"
]

