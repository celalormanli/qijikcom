from django.shortcuts import render
from rest_framework.response import Response
from word_memorization.serializers import WordSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from word_memorization.models import Word, Category

@api_view(['GET'])
def word_list(request):
    if request.method=='GET':
        words =  Word.objects.all()
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
        categories=Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)