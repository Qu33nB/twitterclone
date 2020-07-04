from django.db import models
from django.utils import timezone
from twitteruser.models import CustomUser

# Create your models here.
class Tweet(models.Model):
    author = models.ForeignKey(CustomUser, default=None, on_delete=models.CASCADE)
    tweet = models.CharField(max_length=140)
    up_votes = models.IntegerField(default=0, blank=True, null=True)
    down_votes = models.IntegerField(default=0, blank=True, null=True)
    submission_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tweet