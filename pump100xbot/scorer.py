# scorer.py

from config import *

def parse_number(val):
    val = val.replace(",", "").replace("$", "")
    if "K" in val:
        return float(val.replace("K", "")) * 1000
    if "M" in val:
        return float(val.replace("M", "")) * 1_000_000
    return float(val)

def score_token(token):
    score = 0

    mc = parse_number(token["marketcap"])
    vol = parse_number(token["volume"])
    holders = token["holders"]
    curve = token["curve"]

    if mc <= MAX_MARKETCAP: score += 15
    if vol >= MIN_VOLUME: score += 15
    if holders >= MIN_HOLDERS: score += 20
    if curve <= MAX_CURVE: score += 20

    # Bonus untuk MC sangat kecil
    if mc < 10000: score += 10

    return score

