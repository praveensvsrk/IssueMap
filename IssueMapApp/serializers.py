from rest_framework import serializers
from IssueMapApp.models import *

class IssueSerializer(serializers.Serializer):

    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Issue
        fields = ('id', 'longitude', 'latitude', 'description','department','severity','creation_date','username','image')
