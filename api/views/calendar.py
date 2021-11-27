from rest_framework import generics, serializers, status
from rest_framework.response import Response

from content.models.sentence import Sentence


class CalendarListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sentence
        fields = ('user_id', 'sentence', 'date', 'title', 'date_m')


class CalendarListView(generics.ListAPIView):
    queryset = Sentence.objects.all()
    serializer_class = CalendarListSerializer

    def get(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id', None)
        # tweet_list, df = twitter_user(user_id)

        queryset = self.get_queryset().filter(user_id=user_id)  # 필터 추가, 이름만 가져온다. sql where userid = name

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        return Response(
            data={
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
            # headers=headers,
        )
