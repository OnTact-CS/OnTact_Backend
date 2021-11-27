from django.conf.urls import url

from .views import UserListView
from .views import SentenceListView
from .views import WordListView
from .views import CalendarListView
from .views import TempAvgListView
from .views import WordTempListView

app_name = 'api'


urlpatterns = [
    url(r'^user/$', UserListView.as_view(), name='user'),
    url(r'^sentence$', SentenceListView.as_view(), name='sentence'),
    url(r'^word/$', WordListView.as_view(), name='word'),
    url(r'^calendar/$', CalendarListView.as_view(), name='calendar'),
    url(r'^temp_avg/$', TempAvgListView.as_view(), name='tempavg'),
    url(r'^word_temp/$', WordTempListView.as_view(), name='wordtemp'),
]