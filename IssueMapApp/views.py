from django.http import HttpResponse
from django.db.models import Q
from IssueMapApp.models import *
from IssueMapApp.serializers import IssueSerializer, DepartmentSerializer
from rest_framework import generics


class IssueList(generics.ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def get_queryset(self):
        cur_lat = float(self.request.GET.get('lat'))
        cur_long = float(self.request.GET.get('long'))
        offset = float(self.request.GET.get('offset'))

        min_lat = cur_lat - offset
        max_lat = cur_lat + offset
        min_long = cur_long - offset
        max_long = cur_long + offset

        print(min_lat, min_long, max_lat, max_long)

        return Issue.objects.filter(
            Q(latitude__gte=min_lat)
            & Q(latitude__lte=max_lat)
            & Q(longitude__gte=min_long)
            & Q(longitude__lte=max_long))


class NewIssue(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class IssueDetail(generics.RetrieveUpdateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

def index(request):
    return HttpResponse("hello")


