from django.db import IntegrityError
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth.forms import PasswordResetForm
# from django.core.mail import send_mail
# from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.conf import settings

# from .forms import ProducerRegistrationForm, ProducerForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def logout_view(request):
    logout(request)
    return redirect('home2')


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
                user.last_name = last_name
                user.save()
                profile = UserProfile.objects.create(
                    user=user,
                    middle_name=middle_name,
                    country_code=country_code,
                    phone_number=phone_number,
                    address1=address1,
                    address2=address2,
                    city=city,
                    state=state,
                    country=country,
                    zip_code=zip_code
                )
                profile.save()
                login(request, user)
                return redirect('home2')
            except IntegrityError:
                return render(request, 'register.html', {'error': 'Username or email already exists'})
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    return render(request, 'register.html')


class ForgotPasswordView(PasswordResetView):
    template_name = 'forgotpassword'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Send a custom confirmation email if needed
        email = form.cleaned_data.get('email')
        send_mail(
            'Password Reset Request',
            'We have received a request to reset your password. Please check your email for further instructions.',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        return response


def home2(request):
    return render(request, 'home2.html')
