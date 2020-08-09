from django.contrib import admin
from .models import UserOffer

class UserOfferAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(UserOffer, UserOfferAdmin)
