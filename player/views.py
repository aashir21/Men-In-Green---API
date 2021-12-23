from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import T20PlayersSerializer, ODIPlayersSerializer, TestPlayersSerializer
from .models import T20Players, ODIPlayers, TestPlayers
# Create your views here.


@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List': '/t20player-list/',
        'Detail': '/t20player-list/<str:pk>/',
        'Create': '/t20player-create',
        'Update': '/t20player-update/<str:pk>/',
        'Delete': '/t20player-delete/<str:pk>',
        # 'List': '/odiplayer-list/',
        # 'Detail': '/odiplayer-list/<str:pk>/',
        # 'Create': '/odiplayer-create',
        # 'Update': '/odiplayer-update/<str:pk>/',
        # 'Delete': '/odiplayer-delete/<str:pk>',
    }

    return Response(api_urls)


@api_view(['GET'])
def T20playerList(request):
    players = T20Players.objects.all()
    serializer = T20PlayersSerializer(players, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def T20playerDetail(request, pk):
    players = T20Players.objects.get(id=pk)
    serializer = T20PlayersSerializer(players, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def T20playerCreate(request):

    serializer = T20PlayersSerializer(data=request.data)

    if serializer.is_valid:
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def T20playerUpdate(request, pk):

    players = T20Players.objects.get(id=pk)
    serializer = T20PlayersSerializer(instance=players, data=request.data)

    if serializer.is_valid():
        serializer.save

    return Response(serializer.data)


@api_view(['DELETE'])
def T20playerDelete(request, pk):
    players = T20Players.objects.get(id=pk)
    players.delete()

    return Response('PLAYER INFO DELETED!')


@api_view(['GET'])
def ODIplayerList(request):
    players = ODIPlayers.objects.all()
    serializer = ODIPlayersSerializer(players, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def ODIplayerDetail(request, pk):
    players = ODIPlayers.objects.get(id=pk)
    serializer = ODIPlayersSerializer(players, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def ODIplayerCreate(request):

    serializer = ODIPlayersSerializer(data=request.data)

    if serializer.is_valid:
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def ODIplayerUpdate(request, pk):

    players = ODIPlayers.objects.get(id=pk)
    serializer = ODIPlayersSerializer(instance=players, data=request.data)

    if serializer.is_valid():
        serializer.save

    return Response(serializer.data)


@api_view(['DELETE'])
def ODIplayerDelete(request, pk):
    players = ODIPlayers.objects.get(id=pk)
    players.delete()

    return Response('PLAYER INFO DELETED!')


@api_view(['GET'])
def TestplayerList(request):
    players = TestPlayers.objects.all()
    serializer = TestPlayersSerializer(players, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def TestplayerDetail(request, pk):
    players = TestPlayers.objects.get(id=pk)
    serializer = TestPlayersSerializer(players, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def TestplayerCreate(request):

    serializer = TestPlayersSerializer(data=request.data)

    if serializer.is_valid:
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def TestplayerUpdate(request, pk):

    players = TestPlayers.objects.get(id=pk)
    serializer = TestPlayersSerializer(instance=players, data=request.data)

    if serializer.is_valid():
        serializer.save

    return Response(serializer.data)


@api_view(['DELETE'])
def TestplayerDelete(request, pk):
    players = TestPlayers.objects.get(id=pk)
    players.delete()

    return Response('PLAYER INFO DELETED!')
