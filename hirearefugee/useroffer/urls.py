from django.urls import path
from . import views

app_name = 'useroffer'

urlpatterns = [
    path('create/', views.createuseroffer, name='createuseroffer'),
    path('current/', views.currentuseroffers, name='currentuseroffers'),
    path('completed/', views.completeduseroffers, name='completeduseroffers'),
    path('<int:useroffer_pk>/', views.viewuseroffer, name='viewuseroffer'),
    path('<int:useroffer_pk>/complete/', views.completeuseroffer, name='completeuseroffer'),
    path('<int:useroffer_pk>/delete/', views.deleteuseroffer, name='deleteuseroffer'),
]
