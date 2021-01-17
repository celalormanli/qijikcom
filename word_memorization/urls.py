from django.urls import path, include
from word_memorization.views import word_list
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns =[
    path('words/', word_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
