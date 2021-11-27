import pandas as pd
import os
from konlpy.tag import Okt
from content.sentiment.movie_model import sentiment_predict
from content.sentiment.twitter_crawling import twitter_user
import tensorflow as tf
from konlpy.tag import Okt
from timeit import default_timer as timer
from datetime import timedelta
from google.cloud import language_v1

credential_path = 'apt-achievment-321715-b8781b0ad8cf.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path


def word_list(df1):
    okt = Okt()

    morphs = [okt.pos(sentence) for sentence in df1[0]]

    noun_adj_adv_list = []
    append = noun_adj_adv_list.append

    not_word = ["것", "내", "나", "수", "게", "말", "의"]

    for sentence in morphs:
        for word, tag in sentence:
            if tag in ['Noun'] and (word not in not_word):
                append(word)
            if tag in ['Adverb'] and (word not in not_word):
                append(word)
            if tag in ['Adjective'] and (word not in not_word):
                append(word)

    # print(noun_adj_adv_list)

    duple_list = list(set(noun_adj_adv_list))

    change_list = []
    client = language_v1.LanguageServiceClient()

    for s in duple_list:
        if len(s) > 1:
            change_list.append(s)

    word_score_list = ['\0' for i in range(len(change_list))]

    for i in range(len(change_list)):
        sentence_str = str(change_list[i])
        document = language_v1.Document(content=sentence_str, type_=language_v1.Document.Type.PLAIN_TEXT)

        sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
        word_score_list[i] = sentiment.score

    return change_list, word_score_list


# print(word_list(twitter_user("SANDEUL920320")))


def cold_def(df1):
    # start = timer()
    change_list, word_score_list = word_list(df1)
    data = {'Word': change_list, 'Score': word_score_list}
    word_df = pd.DataFrame(data, columns=['Word', 'Score'])
    word_df['Score'] = pd.to_numeric(word_df['Score'])

    cold_word = word_df[word_df['Score'] < 0]
    cold_li = []
    cold_list = cold_word.values.tolist()
    for index, value in enumerate(cold_list):
        # print(value[0])
        value[0] = value[0].strip()
        cold_li.append([value[0], value[1]])

    cold_word_list = [cold_list[i][0] for i in range(len(cold_list))]

    return cold_word_list


# print(cold_def(twitter_user("SANDEUL920320")))


def normal_def(df1):
    change_list, word_score_list = word_list(df1)
    data = {'Word': change_list, 'Score': word_score_list}
    word_df = pd.DataFrame(data, columns=['Word', 'Score'])
    word_df['Score'] = pd.to_numeric(word_df['Score'])

    normal_word = word_df[word_df['Score'] == 0]
    normal_li = []
    normal_list = normal_word.values.tolist()
    for index, value in enumerate(normal_list):
        # print(value[0])
        value[0] = value[0].strip()
        normal_li.append([value[0], value[1]])
    # print(strip_li)
    normal_word_list = [normal_list[i][0] for i in range(len(normal_list))]

    return normal_word_list


def warm_def(df1):
    change_list, word_score_list = word_list(df1)
    data = {'Word': change_list, 'Score': word_score_list}
    word_df = pd.DataFrame(data, columns=['Word', 'Score'])
    word_df['Score'] = pd.to_numeric(word_df['Score'])

    warm_word = word_df[word_df['Score'] > 0]
    warm_li = []
    warm_list = warm_word.values.tolist()
    for index, value in enumerate(warm_list):
        # print(value[0])
        value[0] = value[0].strip()
        warm_li.append([value[0], value[1]])
    # print(strip_li)

    warm_word_list = [warm_list[i][0] for i in range(len(warm_list))]

    return warm_word_list