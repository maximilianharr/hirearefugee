from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('becomeamember/', views.becomeamember, name='becomeamember'),
    path('donate/', views.donate, name='donate'),
    path('helpcoding/', views.helpcoding, name='helpcoding'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('spreadtheword/', views.spreadtheword, name='spreadtheword'),
    path('thanks/', views.thanks, name='thanks'),
]
