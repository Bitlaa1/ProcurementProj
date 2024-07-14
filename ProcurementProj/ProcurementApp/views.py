from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from .forms import ProducerRegistrationForm, LoginForm
from .models import Producer


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def signin(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def userauthenticate(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid credentials")
        else:
            messages.error(request, "Please correct the errors below.")
    return redirect('login')


def register(request):
    form = ProducerRegistrationForm()
    return render(request, 'register.html', {'form': form})


def registerauth(request):
    if request.method == 'POST':
        form = ProducerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the form which returns the user object
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('home')  # Redirect to home page after successful registration
        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, 'register.html', {'form': form})
    else:
        form = ProducerRegistrationForm()

    return render(request, 'register.html', {'form': form})

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
