from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home' ),
    path('signup/', views.signupform, name = 'signup'),
    path('signin/', views.signinform, name='signin'),
    path('password_reset', views.password_reset_request, name='password_reset')
]