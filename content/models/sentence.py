from __future__ import unicode_literals

from django.db import models


# 문장 모델
class Sentence(models.Model):
#    twitter_sen_id = models.IntegerField(blank=False)  # 문장 번호
    user_id = models.CharField(max_length=200)  # user_id
    sentence = models.CharField(max_length=500)  # 문장
    date = models.DateField(auto_now=False)  # 트윗이 생성된 날짜
    title = models.FloatField(blank=False)  # 점수
    date_m = models.CharField(max_length=200)

    def __str__(self):
        return self.sentence
