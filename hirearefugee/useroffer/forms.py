from django.forms import ModelForm
from .models import UserOffer

class UserOfferForm(ModelForm):
    class Meta:
        model = UserOffer
        fields = ['title', 'memo', 'important']
