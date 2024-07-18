# # ProcurementApp/models.py
# from django.db import models
# from django.contrib.auth.models import User
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     middle_name = models.CharField(max_length=30, blank=True)
#     country_code = models.CharField(max_length=10, blank=True)
#     phone_number = models.CharField(max_length=15, blank=True)
#     address1 = models.CharField(max_length=255, blank=True)
#     address2 = models.CharField(max_length=255, blank=True)
#     city = models.CharField(max_length=50, blank=True)
#     state = models.CharField(max_length=50, blank=True)
#     country = models.CharField(max_length=50, blank=True)
#     zip_code = models.CharField(max_length=10, blank=True)
#
#
# def __str__(self):
#     return self.user.username
#
#
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
