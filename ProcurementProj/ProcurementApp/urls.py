from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('registerauth/', views.registerauth, name='registerauth'),
    path('loginauth/', views.loginauth, name='registerauth'),
]