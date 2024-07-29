from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('home2', views.home2, name='home2'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact_us'),
    path('contact-success/', views.contact_success, name='contact_success'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('userauthenticate/', views.userauthenticate, name='userauthenticate'),
    # path('registerauth/', views.registerauth, name='registerauth'),
    path('register/', views.register, name='register'),
    path('get_contact_messages/', views.get_contact_messages, name='get_contact_messages'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', views.profile, name='profile'),
    path('index', views.index, name='index'),
    path('place_order/', views.place_order, name='place_order'),
    path('checkout/', views.checkout, name='checkout'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('get_started/', views.get_started, name='get_started'),
    path('learn_more/', views.learn_more, name='learn_more'),
    path('carbonfootprintcalculator/', views.carbon_footprint_calculator, name='carbonfootprintcalculator'),
    path('sustainability_guidelines/', views.sustainability_guidelines, name='sustainability_guidelines'),
    path('agricultural_best_practices/', views.agricultural_best_practices, name='agricultural_best_practices'),
    path('tips_water_management/', views.tips_water_management, name='tips_water_management'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('service_terms/', views.service_terms, name='service_terms'),
    path('setting_nav/', views.setting_nav, name='setting_nav'),
    path('supplier_register/', views.supplier_register, name='supplier_register'),
    path('supplier_login/', views.supplier_login, name='supplier_login'),
    path('supplier_home/', views.supplier_home, name='supplier_home'),
]