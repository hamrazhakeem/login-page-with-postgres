from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.signin,name = 'signin'),
    path('signup',views.signup,name = 'signup'),
    path('home',views.home,name = 'home'),
    path('signout',views.signout,name = 'signout'),
    path('profile',views.profile,name = 'profile'),
]
