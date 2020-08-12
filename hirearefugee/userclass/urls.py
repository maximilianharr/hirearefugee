from django.urls import path
from . import views

app_name = 'userclass'

urlpatterns = [
    path('details/', views.details, name='details'),
]
