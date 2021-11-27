from rest_framework import generics, serializers, status
from rest_framework.response import Response

from content.models.word import Word


# 모임 리스트 시리얼라이저. api에서 보여줄 필드 명시
from content.sentiment.twitter_crawling import twitter_date, count_word, twitter_user


class WordListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ('word_user_id', 'text', 'value')

    def create(self, validated_data):  # 문장을 만든다...?
        my_incoming_data = validated_data

        # If you want to pop any field from the incoming data then you can like below.
        # popped_data = validated_data.pop('timeFrames')

        inserted_data = Word.objects.create(**validated_data)

        return Response(inserted_data)


# api/moim 으로 get하면 이 listview로 연결
class WordListView(generics.ListAPIView):
    queryset = Word.objects.all()
    serializer_class = WordListSerializer

    def get(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id', None)
        queryset = self.get_queryset().filter(word_user_id=user_id)  # 필터 추가, 이름만 가져온다. sql where userid = name

        tweet_list, df = twitter_user(user_id)
        words_dic, noun_adj_adv_list = count_word(df)
#        words, noun_adj_adv_list = count_word(twitter_date(user_id, '2020-12'))

#        wdf = twitter_date("SANDEUL920320", '2020-12')
#        for i in range(len(words.keys())):

#            wt = (wdf['Tweets'][i], wdf['Dates'][i])
#            ww.append(wt)

        for key, value in words_dic.items():
            Word.objects.create(word_user_id=user_id, text=key, value=value)

#        ww = Word.objects.values('text', 'value')  #sql select word, word_count

#        wdf = noun_adj_adv_list

#        for i in range(len(noun_adj_adv_list)):
#            Word.objects.create(sen_id=i, word_date='2020-12', word=noun_adj_adv_list[i][0], word_count=words[i][1])

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        # headers = self.get_success_headers(serializer.data)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(
            data={
#                "word_index": 201,
                #                "message": twitter_date("SANDEUL920320", '2020-12'),
                #                "message": twitter_date(user_id, '2020-12'),
#                "sen_id": twitter_date("SANDEUL920320", '2020-12'),
#                "word_date": 2020-12,
#                "word": noun_adj_adv_list,
#                "word_count": words
                "data": serializer.data,
##                "data": ww
            },
            status=status.HTTP_201_CREATED,
            # headers=headers,
        )
