from rest_framework import serializers
from word_memorization.models import Word

class WordSerializer(serializers.Serializer):
    english = serializers.CharField(required=False, allow_blank=False,max_length=100)
    turkish = serializers.CharField(required=False, allow_blank=False,max_length=100)
    german = serializers.CharField(required=False, allow_blank=False,max_length=100)
    french = serializers.CharField(required=False, allow_blank=False,max_length=100)
