from django import forms
from .models import ContactMessage


# from django.contrib.auth.models import User
# from .models import Producer
#
#
# class ProducerRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
#
#         if password != confirm_password:
#             raise forms.ValidationError("Passwords do not match")
#         return cleaned_data
#
#
# class ProducerForm(forms.ModelForm):
#     class Meta:
#         model = Producer
#         fields = ['first_name', 'middle_name', 'last_name', 'country_code', 'contact_number', 'address1', 'address2',
#                   'city', 'state', 'country', 'zip_code']
#
# # class CustomPasswordResetForm(PasswordResetForm):
# #     email = forms.EmailField(max_length=100)

class OrderForm(forms.Form):
    product_pic = forms.CharField(max_length=255)
    product_name = forms.CharField(max_length=255)
    product_description = forms.CharField(widget=forms.Textarea)
    quantity = forms.IntegerField()


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }



class CartForm(forms.Form):
    product = forms.CharField(max_length=255)
