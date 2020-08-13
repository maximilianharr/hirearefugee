from django.urls import path
from . import views

app_name = 'userchat'

urlpatterns = [
    path('show/', views.show, name='show'),
]
