from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.signin, name='login'),
    path('userauthenticate/', views.userauthenticate, name='userauthenticate'),
    path('registerauth/', views.registerauth, name='registerauth'),
    path('register/', views.register, name='register'),
    # path('forgot_password/', views.forgot_password, name='forgot_password'),
]