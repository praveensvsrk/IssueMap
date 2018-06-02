from django.db import models
from django.contrib.auth.models import User



class Issue(models.Model):
    id = models.AutoField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    description = models.TextField(max_length=500)
    department = models.CharField(max_length=20)
    severity = models.IntegerField()
    creation_date = models.DateField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Images/', default='Images/None/no-img.jpg')

    def __str__(self):
        return self.id
