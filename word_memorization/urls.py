from django.urls import path, include
from word_memorization.views import word_list, word_list_filtered
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns =[
    path('words/', word_list),
    path('words/<str:fk>', word_list_filtered),
]

urlpatterns = format_suffix_patterns(urlpatterns)
