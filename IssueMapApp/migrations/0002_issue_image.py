# Generated by Django 2.0.6 on 2018-06-02 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IssueMapApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='image',
            field=models.ImageField(default='Images/None/no-img.jpg', upload_to='Images/'),
        ),
    ]
