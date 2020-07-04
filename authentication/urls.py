from django.urls import path
from authentication import views

urlpatterns = [ 
    path('login/', views.signin),
    path('signup/', views.signup),
    path('signout/', views.signout),
]
