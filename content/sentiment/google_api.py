from pprint import pprint

import tweepy
from konlpy.tag import Twitter
import re
import pandas as pd
import numpy as np
import os
from google.cloud import language_v1

from content.sentiment.twitter_crawling import twitter_user
from content.sentiment.movie_model import sentiment_predict

credential_path = 'apt-achievment-321715-b8781b0ad8cf.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path
# Imports the Google Cloud client library


def tweet_sentiment(name):
    client = language_v1.LanguageServiceClient()

    tweet_list, df = twitter_user(name)

    score_list = ['\0' for i in range(len(tweet_list))]

    for i in range(len(tweet_list)):
        sentence_str = str(tweet_list[i])

        document = language_v1.Document(content=sentence_str, type_=language_v1.Document.Type.PLAIN_TEXT)

        sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
        score_list[i] = format((sentiment.score+1)*25+sentiment_predict(sentence_str)*50, ".1f")
    #   print("Text: {}".format(sentence_str.strip("['']")))
    #    print("Sentiment: (score) {}   (magnitude) {}".format(sentiment.score, sentiment.magnitude))

#    return sentiment.score, sentence_str.strip("['']")
#     return score_list, sentiment.magnitude
    return score_list


# if __name__ == "__main__":
    # execute only if run as a script
    # tweet_sentiment()


#print(tweet_sentiment("SANDEUL920320"))
