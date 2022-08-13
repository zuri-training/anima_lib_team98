from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home' ),
    path('signup/', views.signupform, name = 'signup'),
    path('signin/', views.signinform, name='signin'),
    path('logout/', views.logoutUser, name='logout'),
    path('about/', views.about, name='about'),
    # path('documentation/', views.documentation, name='documentation'),
    path('animation/', views.animation, name='animation'),
    path('faq/', views.faq, name='faq'),
    path('doc_type1/', views.doc_page1, name='doc_page1'),
    path('doc_type2/', views.doc_page2, name='doc_page2'),
    path('doc_type3/', views.doc_page3, name='doc_page3'),
    path('doc_page4/', views.doc_page4, name='doc_page4')
]