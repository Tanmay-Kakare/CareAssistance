from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('login', views.login_user, name='login'),
    path('signup', views.signup, name='signup'),
]