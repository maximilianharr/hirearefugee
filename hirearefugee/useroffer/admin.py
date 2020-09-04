from django.contrib import admin
from .models import UserOffer

# Make some readonly fields visible in admin page
class UserOfferAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(UserOffer, UserOfferAdmin)
