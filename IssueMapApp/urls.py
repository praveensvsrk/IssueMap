from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from IssueMapApp import views

urlpatterns = [
    path('home/', views.index),
]
