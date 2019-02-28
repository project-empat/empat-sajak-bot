from os import environ

'''
Local Settings for _empat_sajak account. 
'''

# Configuration for Twitter API
ENABLE_TWITTER_POSTING = environ.get('TWITTER_POSTING', "Y")  # Tweet resulting status?
MY_CONSUMER_KEY = environ.get('TWITTER_CONSUMER_KEY')  # Your Twitter API Consumer Key set in Heroku config
MY_CONSUMER_SECRET = environ.get('TWITTER_CONSUMER_SECRET')  # Your Consumer Secret Key set in Heroku config
MY_ACCESS_TOKEN_KEY = environ.get('TWITTER_ACCESS_TOKEN_KEY')  # Your Twitter API Access Token Key set in Heroku config
MY_ACCESS_TOKEN_SECRET = environ.get('TWITTER_ACCESS_SECRET')  # Your Access Token Secret set in Heroku config
ODDS = 0  # How often do you want this to run? 1/8 times?

DEBUG = environ.get('BOT_DEBUG', "Y")  # Set this to False to start Tweeting live

DATA_SOURCE_FOLDER = "source/"
DATA_SOURCE_HASH = "bb02d06adc914d7cb4196aff5a542d089a003f0edd325e7e402dc97aa02993a9"
MARKOV_MODEL_JSON = "model/model.json"
