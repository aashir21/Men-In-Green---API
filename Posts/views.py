
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Articles
from .serializers import ArticleSerializer
# Create your views here.


@api_view(['GET'])
def apiOverView(request):

    api_urls = {
        'List': '/article-list/',
        'Detail': '/article-detail/<str:pk>',
        'Create': '/article-create',
        'Update': '/article-update/<str:pk>',
        'Delete': '/article-delete/<str:pk>'
    }

    return Response(api_urls)


@api_view(['GET'])
def articleList(request):
    articles = Articles.objects.all()
    serializer = ArticleSerializer(articles, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def articleDetail(request, pk):
    articles = Articles.objects.get(id=pk)
    serializer = ArticleSerializer(articles, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def articleCreate(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def articleUpdate(request, pk):
    articles = Articles.objects.get(id=pk)
    serializer = ArticleSerializer(instance=articles, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def articleDelete(request, pk):
    articles = Articles.objects.get(id=pk)
    articles.delete()

    return Response('ARTICLE DELETED')
