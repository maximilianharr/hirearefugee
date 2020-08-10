from django.urls import path
from . import views

app_name = 'message'

urlpatterns = [
    path('show/', views.show, name='show'),
]
