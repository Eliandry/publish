from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('news/', news_list, name='news_list'),
    path('news/<int:pk>/', news_detail, name='news_detail'),
    path('articles/', article_list, name='article_list'),
    path('articles/<int:pk>/', article_detail, name='article_detail'),
    path('terms/',terms_list,name='terms'),
    path('history/', history_list, name='history_list'),
    path('history/<int:pk>/', history_detail, name='history_detail'),
]
