from django.db.models import Avg
from rest_framework import generics, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from time import strftime

from content.models.sentence import Sentence
from content.sentiment.google_api import tweet_sentiment
from content.sentiment.twitter_crawling import twitter_user

import pandas as pd

# 모임 리스트 시리얼라이저. api에서 보여줄 필드 명시


class SentenceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sentence
        fields = ('user_id', 'sentence', 'date', 'title', 'date_m')

    def create(self, validated_data):  # 문장을 만든다...?
        my_incoming_data = validated_data

        # If you want to pop any field from the incoming data then you can like below.
        # popped_data = validated_data.pop('timeFrames')

        inserted_data = Sentence.objects.create(**validated_data)

        return Response(inserted_data)


class SentenceListView(generics.ListAPIView):
    queryset = Sentence.objects.all()  # 전체 sentence를 가져온다.
    serializer_class = SentenceListSerializer

    def get(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id', None)

        tweet_list, df = twitter_user(user_id)
        score = tweet_sentiment(user_id)
        ss = []

        for i in range(len(df)):
            st = (df['Tweets'][i], df['Dates'][i])
            ss.append(st)

        for i in range(len(df)):
            Sentence.objects.get_or_create(user_id=user_id, sentence=ss[i][0], date=ss[i][1], title=score[i], date_m=(ss[i][1]).strftime('%Y-%m'))

        queryset = self.get_queryset().filter(user_id=user_id)  # 필터 추가, 이름만 가져온다. sql where userid = name

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        # headers = self.get_success_headers(serializer.data)

        #format(('date', "%Y-%m-%d"), "%Y-%m")
        total_sen = self.get_queryset().filter(user_id=user_id).count()
        avg_sen = self.get_queryset().filter(user_id=user_id).aggregate(Avg('title'))

        avg_sen['total_sen'] = total_sen
        avg_month = self.get_queryset().filter(user_id=user_id).values('date_m').annotate(Avg('title'))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(
            data={
#                "status": 201, {"total_sen": total_sen})
#                "total": {"total_sen": total_sen},
                "avg": avg_sen,
                "m_avg": avg_month,
                "data": serializer.data,
#                "data": score,
#                "user_id": user_id,
            },
            status=status.HTTP_201_CREATED,
            # headers=headers,
        )
