from django.urls import path
from . import views

app_name = 'userchat'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('show/', views.show, name='show'),
    path('<str:room_name>/', views.room, name='room'),
]
