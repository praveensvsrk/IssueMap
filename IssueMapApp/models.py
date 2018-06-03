from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    twitter_handles = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Issue(models.Model):
    id = models.AutoField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    description = models.TextField(max_length=500)
    # department = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    severity = models.IntegerField()
    creation_date = models.DateField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Images/', default='Images/None/no-img.jpg')
    tweet_id = models.CharField(max_length=128, null=True)
    status = models.IntegerField()

    def __str__(self):
        return self.id
