from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home' ),
    path('signup/', views.signupform, name = 'signup'),
    path('signin/', views.signinform, name='signin'),
    path('logout/', views.logoutUser, name='logout'),
    path('about/', views.about, name='about'),
    path('documentation/', views.documentation, name='documentation'),
    path('animation/', views.animation, name='animation')
]