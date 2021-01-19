from django.urls import path, include
from word_memorization.views import word_list, word_list_filtered, category_list
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns =[
    path('words/', word_list),
    path('words/<str:fk>', word_list_filtered),
    path('categories/', category_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
