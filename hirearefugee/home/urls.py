from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('agb/', views.agb, name='agb'),
    path('cookies/', views.imprint, name='cookies'),
    path('community/', views.community, name='community'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('imprint/', views.imprint, name='imprint'),
    path('testhtml/', views.testhtml, name='testhtml'),
]
