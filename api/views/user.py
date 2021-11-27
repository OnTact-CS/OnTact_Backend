import tweepy
from rest_framework import generics, serializers
from rest_framework.response import Response
from rest_framework import status
from content.models import User
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


# 모임 리스트 시리얼라이저. api에서 보여줄 필드 명시
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('twitter_id', 'name', 'twitter_user_url', 'description', 'user_created', 'profile_img')

    def create(self, validated_data):  # 문장을 만든다...?
        my_incoming_data = validated_data

        # If you want to pop any field from the incoming data then you can like below.
        # popped_data = validated_data.pop('timeFrames')

        inserted_data = User.objects.create(**validated_data)

        return Response(inserted_data)


# api/moim 으로 get하면 이 listview로 연결
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get(self, request):
        user_id = request.GET.get('user_id', None)
        queryset = self.get_queryset().filter(twitter_id=user_id)  # 필터 추가, 이름만 가져온다. sql where userid = name

        user_api = api.get_user(user_id)
        user_url = (user_api.profile_image_url).replace("_normal", "")

        User.objects.get_or_create(twitter_id=user_id, name=user_api.name, twitter_user_url='https://twitter.com/'+user_id, description=user_api.description, user_created=user_api.created_at, profile_img=user_url)

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page)
            return self.get_paginated_response(serializer.data)

        return Response(
            data={
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
            # headers=headers,
        )
