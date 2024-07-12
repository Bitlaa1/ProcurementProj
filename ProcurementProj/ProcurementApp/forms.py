from django import forms
from django.contrib.auth.models import User
from .models import Producer


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class ProducerRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Producer
        fields = ['company_name', 'address', 'contact_number', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        producer = Producer(
            user=user,
            company_name=self.cleaned_data['company_name'],
            address=self.cleaned_data['address'],
            contact_number=self.cleaned_data['contact_number'],
            email=self.cleaned_data['email']
        )
        if commit:
            producer.save()
        return producer