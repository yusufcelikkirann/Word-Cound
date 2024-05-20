from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('word-count', views.word_count, name='word_count_page')
]
 