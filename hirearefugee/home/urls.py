from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('community/', views.community, name='community'),
    path('settings/', views.settings, name='settings'),
    path('testhtml/', views.testhtml, name='testhtml'),
]
