from django.urls import path
from .views import (articleList, articleDetail, articleCreate,
                    articleUpdate, articleDelete, apiOverView)


urlpatterns = [
    path('', apiOverView),
    path('article-list/', articleList, name='article-list'),
    path('article-detail/<str:pk>', articleDetail, name='article-detail'),
    path('article-create/', articleCreate, name='article-create'),
    path('article-update/<str:pk>', articleUpdate, name='article-update'),
    path('article-delete/<str:pk>', articleDelete, name='article-delete'),

]
