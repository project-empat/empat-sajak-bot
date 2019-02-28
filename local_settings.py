from os import environ

'''
Local Settings for _empat_sajak account. 
'''

# Configuration for Twitter API
ENABLE_TWITTER_SOURCES = False  # Fetch twitter statuses as source
ENABLE_TWITTER_POSTING = True  # Tweet resulting status?
MY_CONSUMER_KEY = environ.get('TWITTER_CONSUMER_KEY')  # Your Twitter API Consumer Key set in Heroku config
MY_CONSUMER_SECRET = environ.get('TWITTER_CONSUMER_SECRET')  # Your Consumer Secret Key set in Heroku config
MY_ACCESS_TOKEN_KEY = environ.get('TWITTER_ACCESS_TOKEN_KEY')  # Your Twitter API Access Token Key set in Heroku config
MY_ACCESS_TOKEN_SECRET = environ.get('TWITTER_ACCESS_SECRET')  # Your Access Token Secret set in Heroku config
ODDS = 0  # How often do you want this to run? 1/8 times?

DEBUG = True  # Set this to False to start Tweeting live
TWEET_ACCOUNT = ""  # The name of the account you're tweeting to.

DATA_SOURCE_FOLDER = "source/"
MARKOV_MODEL_JSON = "model/model.json"
