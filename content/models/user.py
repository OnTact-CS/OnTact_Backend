from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# 간단한 모델 구성
class User(models.Model):   #name, screen_name, description, created_at,followers_count, friends_count,profile_image_url
    twitter_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    twitter_user_url = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    user_created = models.DateField(auto_now=False)
    profile_img = models.CharField(max_length=500)

    def __str__(self):
        return self.name
