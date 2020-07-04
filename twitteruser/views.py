from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from twitteruser.models import CustomUser
from notification.models import Notification


@login_required
def index(request):
    tweets = Tweet.objects.filter(author__in=request.user.followers.all())
    notifications = Notification.objects.filter(recipient=request.user)
    return render(request, 'index.htm', {'tweets': tweets, 'notifications': notifications})
