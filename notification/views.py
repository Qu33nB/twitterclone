from django.shortcuts import render
from notification.models import Notification
from twitteruser.models import CustomUser

# Create your views here.
def notifications(request):
    alerts = list(Notification.objects.filter(recipient=request.user))
    Notification.objects.filer(recipient=request.user).delete()
    users = CustomUser.objects.all()

    return render(request, 'notifications.htm', {'alerts': alerts, 'users': users})
