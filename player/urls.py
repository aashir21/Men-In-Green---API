from django.urls import path
from rest_framework import views
from .views import (apiOverView, T20playerList, T20playerDetail, T20playerCreate, T20playerUpdate, T20playerDelete,
                    ODIplayerList, ODIplayerDetail, ODIplayerUpdate, ODIplayerCreate, ODIplayerDelete,
                    TestplayerList, TestplayerDetail, TestplayerUpdate, TestplayerCreate, TestplayerDelete)

urlpatterns = [
    path('', apiOverView),
    path('t20player-list/', T20playerList, name='t20player-list'),
    path('t20player-detail/<str:pk>', T20playerDetail, name='t20player-detail'),
    path('t20player-create/', T20playerCreate, name='t20player-create'),
    path('t20player-update/<str:pk>', T20playerUpdate, name='t20player-update'),
    path('t20player-delete/<str:pk>', T20playerDelete, name='t20player-delete'),
    path('odiplayer-list/', ODIplayerList, name='odiplayer-list'),
    path('odiplayer-detail/<str:pk>', ODIplayerDetail, name='odiplayer-detail'),
    path('odiplayer-create/', ODIplayerCreate, name='odiplayer-create'),
    path('odiplayer-update/<str:pk>', ODIplayerUpdate, name='odiplayer-update'),
    path('odiplayer-delete/<str:pk>', ODIplayerDelete, name='odiplayer-delete'),
    path('testplayer-list/', TestplayerList, name='testplayer-list'),
    path('testplayer-detail/<str:pk>',
         TestplayerDetail, name='testplayer-detail'),
    path('testplayer-create/', TestplayerCreate, name='testplayer-create'),
    path('testplayer-update/<str:pk>',
         TestplayerUpdate, name='testplayer-update'),
    path('testplayer-delete/<str:pk>',
         TestplayerDelete, name='testplayer-delete'),
]
