from django.shortcuts import render
from rest_framework.response import Response
from word_memorization.serializers import WordSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from word_memorization.models import Word, Category
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL=getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)

@api_view(['GET'])
def word_list(request):
    if request.method=='GET':
        words=None
        if 'words' in cache:
            words =  cache.get('words')    
        else:
            words =  Word.objects.all()
            cache.set('words', words, timeout=CACHE_TTL)
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def word_list_filtered(request, fk):
    if request.method=='GET':
        words=Word.objects.filter(category_name=fk)
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def category_list(request):
    if request.method=='GET':
        categories=None
        if 'categories' in cache:
            categories=cache.get('categories')
        else:
            categories=Category.objects.all()
            cache.set('categories',categories, timeout=CACHE_TTL)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)