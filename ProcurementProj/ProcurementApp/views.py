from django.db import IntegrityError
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import Profile, Order, Feedback, Cart, ContactMessage
from .forms import OrderForm, FeedbackForm, CartForm, ContactMessageForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# from .forms import ProducerRegistrationForm, ProducerForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages = ContactMessage.objects.all()  # Fetch all messages
            return render(request, 'contact_success.html', {'messages': messages})
    else:
        form = ContactMessageForm()
    return render(request, 'contact.html', {'form': form})


def contact_success(request):
    return render(request, 'contact_success.html')


def logout_view(request):
    logout(request)
    return redirect('home2')


def get_contact_messages(request):
    messages = ContactMessage.objects.all().values('name', 'email', 'message')
    return JsonResponse(list(messages), safe=False)


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


def profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        # Ensure the user object is available
        user = request.user

        # Update user fields
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email
        if phone_number:
            # Assuming you have a profile model to handle additional fields
            profile, created = Profile.objects.get_or_create(user=user)
            profile.phone_number = phone_number
            profile.save()

        try:
            user.save()
            messages.success(request, 'Profile updated successfully')
        except IntegrityError as e:
            messages.error(request, f'Error updating profile: {e}')
            return redirect('profile')

        return redirect('profile')

    return render(request, 'profile.html')


def index(request):
    return render(request, 'index.html')


def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Order.objects.create(**data)
            messages.success(request, 'Order placed successfully!')
            return redirect('index')
        else:
            messages.error(request, 'All fields are required!')
    else:
        form = OrderForm()

    return render(request, 'place_order.html', {'form': form})


def checkout(request):
    if request.method == 'POST':
        return redirect('index')
    order_details = request.GET.get('order_details')
    return render(request, 'checkout.html', {'order_details': order_details})


def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Feedback.objects.create(**data)
            messages.success(request, 'Feedback submitted successfully!')
            return redirect('index')
        else:
            messages.error(request, 'All fields are required!')
    else:
        form = FeedbackForm()

    return render(request, 'submit_feedback.html', {'form': form})


def add_to_cart(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product']
            Cart.objects.create(product_name=product_name)
            messages.success(request, 'Product added to cart!')
    return redirect('home2')


def get_started(request):
    return render(request, 'get_started.hml')


def learn_more(request):
    return render(request, 'learn_more.html')


def carbon_footprint_calculator(request):
    if request.method == 'POST':
        energy_usage = float(request.POST.get('energyUsage', 0))
        miles_driven = float(request.POST.get('milesDriven', 0))
        waste_generated = float(request.POST.get('wasteGenerated', 0))

        energy_factor = 0.233
        mileage_factor = 0.211
        waste_factor = 0.3

        energy_emissions = energy_usage * energy_factor
        mileage_emissions = miles_driven * mileage_factor
        waste_emissions = waste_generated * waste_factor
        total_emissions = energy_emissions + mileage_emissions + waste_emissions

        return render(request, 'carbon_footprint.html', {
            'total_emissions': total_emissions
        })

    return render(request, 'carbon_footprint.html')


def sustainability_guidelines(request):
    return render(request, 'sustainability_guidelines.html')


def agricultural_best_practices(request):
    return render(request, 'agricultural_best_practices.html')


def tips_water_management(request):
    return render(request, 'tips_water_management.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def service_terms(request):
    return render(request, 'service_terms.html')


def setting_nav(request):
    return render(request, 'setting_nav.html')