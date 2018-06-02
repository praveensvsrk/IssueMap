from django.http import HttpResponse

from IssueMapApp.models import Issue
from IssueMapApp.serializers import IssueSerializer
from rest_framework import generics


class IssueList(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class IssueDetail(generics.RetrieveUpdateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


def index(request):
    return HttpResponse("hello")