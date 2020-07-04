# Generated by Django 3.0.7 on 2020-07-04 01:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='followers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
