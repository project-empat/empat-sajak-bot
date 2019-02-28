# empat sajak bot
`empat sajak bot` is a Indonesian poetry generator that uses Markov Chains. 
This bot based on [heroku_ebooks](https://github.com/tommeagher/heroku_ebooks) and [adam](https://github.com/bziarkowski/adam).
To make it simple, this bot don't gather data by reading tweet, or toots, or scraping web. 
But from the data that was picked from my personal preference.
The ability to post to Mastodon is also removed.

See also [twitter bot](https://twitter.com/_empat_sajak).

# Installation
In terminal.
```
git clone https://github.com/project-empat/empat-sajak-bot
cd empat-sajak-bot
```
Install Python requirements.
```
pip install -r requirements.txt
```
Now it should be ready to use.

# Generate poems
To generate poems run:
```
python generate_poems.py
```