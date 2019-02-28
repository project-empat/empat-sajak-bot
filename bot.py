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


if __name__ == "__main__":
    guess = 0
    if ODDS and DEBUG == "N":
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
            if DEBUG == "N":
                print("Post to twitter")
                if ENABLE_TWITTER_POSTING == "Y":
                    try:
                        status = api.PostUpdate(bot_status)
                    except Exception as err:
                        print(err)
            print(bot_status)

        elif not bot_status:
            print("Status is empty, sorry.")
        else:
            print("TOO LONG: " + bot_status)
