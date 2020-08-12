from django import forms
from django.core.files.images import get_image_dimensions

from .models import UserDetails


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['image', 'is_refugee']
