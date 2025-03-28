from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")
        labels = {
            "username": "User Name",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Id",
        }

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        labels = {
            "username": "User Name",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Id",
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("role", "phone", "age", "health_conditions")
        widgets = {
            "role": forms.Select(choices=[('caregiver', 'Caregiver'), ('elderly', 'Elderly')]),
        }
        labels = {
            "role": "Role",
            "phone": "Phone Number",
            "age": "Age",
            "health_conditions": "Health Conditions",
        }