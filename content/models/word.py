from __future__ import unicode_literals

from django.db import models
from content.models.sentence import Sentence

# 단어 모델
from django.db.models import ForeignKey


class Word(models.Model):
    word_user_id = models.CharField(max_length=200)    #sen_id 말고 user_id로 수정필요
#    word_date = models.DateField(auto_now=False, default=0000-00-00)  # 트윗이 생성된 날짜
    text = models.CharField(max_length=200) #word->text
    value = models.IntegerField(blank=False)   #word_count->value

    def __str__(self):
        return self.text
