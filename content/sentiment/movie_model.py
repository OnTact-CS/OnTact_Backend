from timeit import default_timer as timer
from datetime import timedelta
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import csv
from content.sentiment.twitter_crawling import twitter_user
import tensorflow as tf
from tensorflow.keras.models import load_model
# physical_devices = tf.config.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)

# loaded_model = load_model('C:\\Users\\YUBIN\\PycharmProjects\\OnPro\\ontact\\my_model.h5')
loaded_model = load_model('my_model.h5')

# with open('C:\\Users\\YUBIN\\PycharmProjects\\OnPro\\ontact\\Encoding.csv', encoding='cp949') as f:
#     reader = csv.reader(f)
#     data = list(reader)

with open('Encoding.csv', encoding='cp949') as f:
    reader = csv.reader(f)
    data = list(reader)

tokenizer = Tokenizer(num_words=12000)
tokenizer.fit_on_texts(data)


def sentiment_predict(new_sentence):
    # start = timer()

    # end = timer()
    # print(timedelta(seconds=end - start))
    #
    # tokenizer = Tokenizer(num_words=12000)
    # tokenizer.fit_on_texts(data)
    # stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']
    # okt = Okt()
    # new_sentence = okt.morphs(new_sentence, stem=True)  # 토큰화
    # new_sentence = [word for word in new_sentence if not word in stopwords]  # 불용어 제거
    encoded = tokenizer.texts_to_sequences([new_sentence])  # 정수 인코딩
    pad_new = pad_sequences(encoded, maxlen=30)  # 패딩
    score = float(loaded_model(pad_new))  # 예측
    # end = timer()
    # print(timedelta(seconds=end - start))

    return score
    #print(format(score*100, ".1f")+"도")


# print(sentiment_predict("안녕 반가워"))


def model_sentiment(name):
    new_list, df1 = twitter_user(name)

    model_score_list = ['\0' for i in range(len(new_list))]

    for i in range(len(new_list)):
        sentence_str = str(new_list[i])

        model_score_list[i] = sentiment_predict(sentence_str)

    return model_score_list


# print(model_sentiment("SANDEUL920320"))

