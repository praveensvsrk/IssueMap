from django.http import HttpResponse
from django.db.models import Q
from IssueMapApp.models import Issue
from IssueMapApp.serializers import IssueSerializer
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

        return Issue.objects.filter(
            Q(latitude__gte=min_lat)
            & Q(latitude__lte=max_lat)
            & Q(latitude__gte=min_long)
            & Q(latitude__lte=max_long))


class IssueDetail(generics.RetrieveUpdateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


def index(request):
    return HttpResponse("hello")
