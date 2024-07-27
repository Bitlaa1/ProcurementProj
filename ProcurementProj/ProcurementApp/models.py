from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    country_code = models.CharField(max_length=5, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # other fields...

    def __str__(self):
        return self.user.username


class Order(models.Model):
    product_pic = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    quantity = models.IntegerField()


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField()


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'


class Cart(models.Model):
    product_name = models.CharField(max_length=255)
