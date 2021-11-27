from rest_framework import generics, serializers, status
from rest_framework.response import Response

from content.models import Word

from content.sentiment.word import cold_def, normal_def, warm_def
from content.sentiment.twitter_crawling import twitter_date, count_word, twitter_user


class WordTempListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('sen_id', 'word', 'word_count')


class WordTempListView(generics.ListAPIView):
    queryset = Word.objects.all()
    serializer_class = WordTempListSerializer

    def get(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id', None)
        # tweet_list, df = twitter_user(user_id)

        return Response(
            data={
                "cold": cold_def(twitter_user(user_id)),
                "normal": normal_def(twitter_user(user_id)),
                "warm": warm_def(twitter_user(user_id))
            },
            status=status.HTTP_201_CREATED,
            # headers=headers,
        )



