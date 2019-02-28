import random
import re
import sys
import twitter
from mastodon import Mastodon
from generate_poems import *

try:
    # Python 3
    from html.entities import name2codepoint as n2c
    from urllib.request import urlopen
except ImportError:
    # Python 2
    from htmlentitydefs import name2codepoint as n2c
    from urllib2 import urlopen

    chr = unichr
from local_settings import *


def connect(type='twitter'):
    if type == 'twitter':
        return twitter.Api(consumer_key=MY_CONSUMER_KEY,
                           consumer_secret=MY_CONSUMER_SECRET,
                           access_token_key=MY_ACCESS_TOKEN_KEY,
                           access_token_secret=MY_ACCESS_TOKEN_SECRET,
                           tweet_mode='extended')
    return None


def entity(text):
    if text[:2] == "&#":
        try:
            if text[:3] == "&#x":
                return chr(int(text[3:-1], 16))
            else:
                return chr(int(text[2:-1]))
        except ValueError:
            pass
    else:
        guess = text[1:-1]
        if guess == "apos":
            guess = "lsquo"
        numero = n2c[guess]
        try:
            text = chr(numero)
        except KeyError:
            pass
    return text


def filter_status(text):
    text = re.sub(r'\b(RT|MT) .+', '', text)  # take out anything after RT or MT
    text = re.sub(r'(\#|@|(h\/t)|(http))\S+', '', text)  # Take out URLs, hashtags, hts, etc.
    text = re.sub('\s+', ' ', text)  # collaspse consecutive whitespace to single spaces.
    text = re.sub(r'\"|\(|\)', '', text)  # take out quotes.
    text = re.sub(r'\s+\(?(via|says)\s@\w+\)?', '', text)  # remove attribution
    text = re.sub(r'<[^>]*>', '', text)  # strip out html tags from mastodon posts
    htmlsents = re.findall(r'&\w+;', text)
    for item in htmlsents:
        text = text.replace(item, entity(item))
    text = re.sub(r'\xe9', 'e', text)  # take out accented e
    return text


if __name__ == "__main__":
    guess = 0
    if ODDS and not DEBUG:
        guess = random.randint(0, ODDS - 1)

    if guess:
        print(str(guess) + " No, sorry, not this time.")  # message if the random number fails.
        sys.exit()
    else:
        api = connect()
        source_statuses = []
        bot_status = generate_poems()

        # throw out tweets that match anything from the source account.
        if bot_status is not None and len(bot_status) < 260:
            if not DEBUG:
                if ENABLE_TWITTER_POSTING:
                    status = api.PostUpdate(bot_status)
            print(bot_status)

        elif not bot_status:
            print("Status is empty, sorry.")
        else:
            print("TOO LONG: " + bot_status)
