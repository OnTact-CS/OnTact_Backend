from django.db.models import Avg
from rest_framework import generics, serializers, status
from rest_framework.response import Response

from content.models.sentence import Sentence
import pandas as pd
import csv
import random


with open('sentence.csv', encoding='cp949') as f:
with open('sentence.csv', encoding='cp949') as f:
    reader = csv.reader(f)
    data = list(reader)


class TempAvgListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sentence
        fields = ('user_id', 'sentence', 'date', 'title', 'date_m')


class TempAvgListView(generics.ListAPIView):
    queryset = Sentence.objects.all()
    serializer_class = TempAvgListSerializer

    def get(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id', None)
        # tweet_list, df = twitter_user(user_id)

        avg_month = self.get_queryset().filter(user_id=user_id).values('date_m').annotate(Avg('title'))  # 필터 추가, 이름만 가져온다. sql where userid = name

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(avg_month, many=True)

        # df1 = pd.DataFrame(avg_month)
        # print(df1['title__avg'])

        # print(df1.sort_values(by=['title__avg'], axis=0))
        # x = (avg_month[1])
        # print(x['title__avg'])
        y1 = 0
        z1 = 0
        msg1 = msg2 = msg3 = ""
        for i in range(len(avg_month)):
            x = (avg_month[i])
            y1 = y1 + 1
            if x['title__avg'] <= 50:
                z1 = z1 + 1
        if y1/2 < z1:
            a = 1
            msg1 = "50도 이하의 결과값이 게시글 수의 1/2보다 많습니다\n"

        for i in range(1, len(avg_month)):
            x = (avg_month[i])
            x2 = (avg_month[i-1])
            if x2['title__avg'] - x['title__avg'] > 25:
                a = 2
                msg2 = (x2['date_m'] + "와 " + x['date_m'] + "의 차이가 25도 이상입니다.\n")

        i = 1
        while i < len(avg_month)-1:
            i = i + 1
            x1 = (avg_month[i - 2])
            x2 = (avg_month[i - 1])
            x3 = (avg_month[i])
            if (x1['title__avg'] > x2['title__avg']) and (x2['title__avg'] > x3['title__avg']):
                msg3 = msg3 + (x1['date_m'] + "부터 ")
                if i + 1 < len(avg_month):
                    while i + 1 < len(avg_month):
                        i = i+1   #8
                        x4 = (avg_month[i])     #8월
                        x3 = (avg_month[i - 1]) #7월
                        if x3['title__avg'] < x4['title__avg']:
                            i = i+1   #9
                            a = 3
                            msg3 = msg3 + (x3['date_m'] + "까지 연속적으로 하락하는 그래프입니다.")
                            break
                        continue
                else:
                    a = 3
                    x_until = avg_month[i]
                    msg3 = msg3 + (x_until['date_m'] + "까지 연속적으로 하락하는 그래프입니다.")

        message = []
        for i in data:
            message.extend(i)

        if a is 1 or a is 2 or a is 3:
            a = random.sample(message, 1)

        return Response(
            data={
                "m_avg": avg_month,
                "msg1": msg1,
                "msg2": msg2,
                "msg3": msg3,
                "msg": a,
            },
            status=status.HTTP_201_CREATED,
            # headers=headers,
        )