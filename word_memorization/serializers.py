from rest_framework import serializers
from word_memorization.models import Word, Category

class WordSerializer(serializers.Serializer):
    english = serializers.CharField(required=False, allow_blank=False,max_length=100)
    turkish = serializers.CharField(required=False, allow_blank=False,max_length=100)
    german = serializers.CharField(required=False, allow_blank=False,max_length=100)
    french = serializers.CharField(required=False, allow_blank=False,max_length=100)


class CategorySerializer(serializers.Serializer):
    category_name = serializers.CharField(required=False, allow_blank=False,max_length=100)
    en = serializers.CharField(required=False, allow_blank=False,max_length=100)
    tr = serializers.CharField(required=False, allow_blank=False,max_length=100)
    de = serializers.CharField(required=False, allow_blank=False,max_length=100)
    fr = serializers.CharField(required=False, allow_blank=False,max_length=100)
