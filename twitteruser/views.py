from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from custom_user.models import CustomUser
from custom_user.forms import SignInForm, SignUpForm
from customUser import settings

# Create your views here.
@login_required
def index(request):
    info = settings.AUTH_USER_MODEL
    return render(request, 'index.html', {'info': info})

def signin(request):
    html = 'generic_form.html'
    
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )
    form = SignInForm()
    return render(request, html, {'form': form})


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def signup(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
                homepage=data['homepage'],
                age=data['age']
            )
            return HttpResponseRedirect(reverse('home'))

    form = SignUpForm()
    return render(request, html, {'form': form})
