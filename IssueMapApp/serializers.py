from rest_framework import serializers

class IssueSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()
    description = serializers.CharField(max_length=500)
    department = serializers.CharField(max_length=20)
    severity = serializers.IntegerField()
    creation_date = serializers.DateField()
    username = serializers.CharField()