# parser.py

from telethon.sync import TelegramClient
from telethon.tl.types import PeerChannel
import re
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("TG_API_ID")
API_HASH = os.getenv("TG_API_HASH")
SESSION = "pump_session"

CHANNEL_USERNAME = "pumpfunvolumeby4AM"  # bisa diganti

def extract_token_data(text):
    pattern = r"\$(\w+).*?MC: \$?([\d,\.Kk]+).*?Holders: (\d+).*?Curve: (\d+)%.*?Volume: \$?([\d,\.Kk]+)"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return {
            "symbol": match.group(1),
            "marketcap": match.group(2),
            "holders": int(match.group(3)),
            "curve": int(match.group(4)),
            "volume": match.group(5)
        }
    return None

def get_new_tokens(limit=10):
    client = TelegramClient(SESSION, API_ID, API_HASH)
    client.start()
    
    result = []
    for message in client.iter_messages(CHANNEL_USERNAME, limit=limit):
        data = extract_token_data(message.text)
        if data:
            result.append(data)
    
    client.disconnect()
    return result

