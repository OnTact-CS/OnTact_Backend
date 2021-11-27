from django.contrib import admin
from .models.user import User
from .models.sentence import Sentence
from .models.word import Word


# Register your models here.
admin.site.register(User)
admin.site.register(Sentence)
admin.site.register(Word)
