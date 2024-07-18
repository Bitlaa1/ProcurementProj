from django.db import IntegrityError

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth.forms import PasswordResetForm
# from django.core.mail import send_mail
# from django.conf import settings
from django.contrib.auth import authenticate, login
# from .forms import ProducerRegistrationForm, ProducerForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home2')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        country_code = request.POST['country_code']
        phone_number = request.POST['phone_number']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        zip_code = request.POST['zip_code']

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = first_name
                # user.middle_name = middle_name
                user.last_name = last_name
                user.save()
                # Assuming you have a UserProfile model for additional fields
                # user.profile.country_code = country_code
                # user.profile.phone_number = phone_number
                # user.profile.address1 = address1
                # user.profile.address2 = address2
                # user.profile.city = city
                # user.profile.state = state
                # user.profile.country = country
                # user.profile.zip_code = zip_code
                # user.profile.save()
                login(request, user)
                return redirect('home2')
            except IntegrityError:
                return render(request, 'register.html', {'error': 'Username or email already exists'})
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    return render(request, 'register.html')


# def forgot_password(request):
#     if request.method == 'POST':
#         password_reset_form = PasswordResetForm(request.POST)
#         if password_reset_form.is_valid():
#             data = password_reset_form.cleaned_data['email']
#             associated_users = User.objects.filter(Q(email=data))
#             if associated_users.exists():
#                 for user in associated_users:
#                     subject = "Password Reset Requested"
#                     email_template_name = "password_reset_email.txt"
#                     c = {
#                         "email": user.email,
#                         'domain': request.META['HTTP_HOST'],
#                         'site_name': 'Your Site',
#                         "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                         "user": user,
#                         'token': default_token_generator.make_token(user),
#                         'protocol': 'http',
#                     }
#                     email = render_to_string(email_template_name, c)
#                     try:
#                         send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
#                     except BadHeaderError:
#                         return HttpResponse('Invalid header found.')
#                     return redirect("password_reset_done")
#     password_reset_form = PasswordResetForm()
#     return render(request, 'forgetpassword.html', {'forget_password': forgot_password()})


def home2(request):
    return render(request, 'home2.html')
