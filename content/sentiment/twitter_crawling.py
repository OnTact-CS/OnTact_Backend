#from wordcloud import Wordcloud
from pprint import pprint

import tweepy
from konlpy.tag import Twitter, Okt
from collections import Counter
import pandas as pd
import numpy as np
import re

from pathlib import Path

import os
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

consumerKey = env('TWITTER_KEY')
consumerSecret = env('TWITTER_SECRET')
accessToken = env('ACCESS_TOKEN_KEY')
accessTokenSecret = env('ACCESS_TOKEN_SECRET')

# Create the authentication object
authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)

# Set the access token and access token secret
authenticate.set_access_token(accessToken, accessTokenSecret)

# Creating the API object while passing in auth information
api = tweepy.API(authenticate, wait_on_rate_limit=True)


def cleanTxt(text):
    text = re.sub('@[A-Za-z0–9]+', ' ', text)    # Removing @mentions
    text = re.sub('#', ' ', text)    # Removing '#' hash tag
    text = re.sub('RT[\s]+', ' ', text)  # Removing RT
    text = re.sub('https?:\/\/\S+', ' ', text)   # Removing hyperlink
    return text


def twitter_user(name):
    sentence_str_connect = ""
#    posts = api.user_timeline(screen_name="B1A4_gongchan", count=100, lang="kr", tweet_mode="extended")
    posts = api.user_timeline(screen_name=name, count=100, lang="kr", tweet_mode="extended")
    data = {'Tweets': [tweet.full_text for tweet in posts], 'Dates': [tweet.created_at for tweet in posts]}
    df = pd.DataFrame(data, columns=['Tweets', 'Dates'])

    df['Tweets'] = df['Tweets'].apply(cleanTxt)
    df['Tweets'] = df['Tweets'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", " ")

# #    pd.set_option('display.max_rows', 100) #colab에서 df 100개 보여주기
#
#     tweet_list = list(np.array(df['Tweets'].tolist()))
#
# #    sentence_str = str(tweet_list)
# #    for i in range(len(tweet_list)):
# #        if (len(sentence_str)):
# #            sentence_str_spc = sentence_str[0]
# #        for index in range(1, len(sentence_str)):
# #            if (sentence_str[inpython manage.py makemigrationsdex - 1] == ' ' and sentence_str[index] == ' '):
# #                continue
# #            sentence_str_spc += sentence_str[index]
# #    pprint(sentence_str_spc)
# #    pprint(df)
#
#     return tweet_list, df
    tweet_list = df.values.tolist()
    strip_li = []
    append = strip_li.append
    for index, value in enumerate(tweet_list):
        # print(value[0])
        value[0] = value[0].strip()
        append([value[0], value[1]])

    code = ''

    strip_li = [i for i in strip_li if not code in i]

    new_list = [strip_li[i][0] for i in range(len(strip_li))]
    # print(new_list)

    df1 = pd.DataFrame(strip_li, columns=['Tweets', 'Dates'])

    return new_list, df1


def twitter_date(name, date):
    tweet_list, df = twitter_user(name)
#    data_filter = df['Dates'] == date
#    date_filter = twitter_user(name).df['Dates'] == date
#    print(df[data_filter])

#    searchfor = [date]
    data_filter = df[df['Dates'].astype(str).str.contains(date)]
#    print(data_filter)
    return data_filter


def count_word(data_filter):

    t = Twitter()
    morphs = []

    for sentence in data_filter['Tweets']:
        morphs.append(t.pos(sentence))

#    print(morphs)

    noun_adj_adv_list = []

    for sentence in morphs:
        for word, tag in sentence:
            if tag in ['Noun'] and ("것" not in word) and ("내" not in word) and ("나" not in word) and ("수" not in word) and ("게" not in word) and ("말" not in word) and ("의" not in word):
                noun_adj_adv_list.append(word)
            if tag in ['Adverb'] and ("것" not in word) and ("내" not in word) and ("나" not in word) and ("수" not in word) and ("게" not in word) and ("말" not in word) and ("의" not in word):
                noun_adj_adv_list.append(word)
            if tag in ['Adjective'] and ("것" not in word) and ("내" not in word) and ("나" not in word) and ("수" not in word) and ("게" not in word) and ("말" not in word) and ("의" not in word):
                noun_adj_adv_list.append(word)

    #    print(noun_adj_adv_list)

    count = Counter(noun_adj_adv_list)

    # words = dict(count.most_common(5))
    # words

    words = dict(count.most_common(80))
#    print(words)
    return words, noun_adj_adv_list


#twitter_date("SANDEUL920320", '2020-12')
#count_word(twitter_user("SANDEUL920320"))
#count_word(twitter_date("SANDEUL920320", '2020-12'))
