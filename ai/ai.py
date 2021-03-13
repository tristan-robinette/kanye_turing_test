import pandas as pd
import markovify
import random
import re
from decouple import config


# URL Dataset goes here.
G_SHEET_URL = config('G_SHEET_URL')


def remove_urls (text):
    text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text, flags=re.MULTILINE)
    return text


# read in data & do some basic processing
df = pd.read_csv(G_SHEET_URL).fillna('')
twitter_model = '\n'.join(df['Text'].tolist())
twitter_model = twitter_model.split('\n')
# removes urls from tweets for training and to increase randomness
tweet_list = [remove_urls(x) for x in twitter_model]
# creates markov model.
twitter_model = markovify.Text(tweet_list, state_size=2)


def is_kanye(status):
    if status == 1:
        tweet = twitter_model.make_sentence()
        return tweet
    else:
        tweet = random.choice(tweet_list)
        return tweet
