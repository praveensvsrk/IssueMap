from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from IssueMapApp import views

urlpatterns = [
    path('home/', views.index),
    path('issuelist/', views.IssueList.as_view()),
    path('new_issue/', views.NewIssue.as_view()),
    path('issuelist/<int:pk>/', views.IssueDetail.as_view()),
    path('departments/', views.DepartmentList.as_view())
]

