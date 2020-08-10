from django.urls import path
from . import views

app_name = 'userauth'

urlpatterns = [
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
]
