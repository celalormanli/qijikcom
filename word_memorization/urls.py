from django.urls import path, include
from word_memorization.views import get_word_list, get_word_list_filtered, get_category_list, add_word, update_word, get_word
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns =[
    path('words/', get_word_list),
    path('words/<str:fk>', get_word_list_filtered),
    path('word/<str:pk>', get_word),
    path('categories/', get_category_list),
    path('addword/', add_word),
]

urlpatterns = format_suffix_patterns(urlpatterns)
