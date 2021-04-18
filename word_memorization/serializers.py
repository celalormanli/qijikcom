from rest_framework import serializers
from word_memorization.models import Word, Category

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields=['english','turkish','german','french']
        write_only_fields = ['category_name']

    def save(self, validated_data):
        category_name = validated_data.pop('category_name')
        category_name = Category.objects.get_or_create(category_name=category_name)[0]
        validated_data['category_name']=category_name
        return Word.objects.create(**validated_data)

    
class CategorySerializer(serializers.Serializer):
    category_name = serializers.CharField(required=False, allow_blank=False,max_length=100)
    en = serializers.CharField(required=False, allow_blank=False,max_length=100)
    tr = serializers.CharField(required=False, allow_blank=False,max_length=100)
    de = serializers.CharField(required=False, allow_blank=False,max_length=100)
    fr = serializers.CharField(required=False, allow_blank=False,max_length=100)
