"""hirearefugee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('userauth/', include('userauth.urls')),

    # Blog
    path('blog/', include('blog.urls')),

    # Home
    path('', home_views.home, name='home'),
    path('home/', include('home.urls')),

    # Message
    path('message/', include('message.urls')),

    # Support
    path('support/', include('support.urls')),

    # Geospatial Data
    path('world/', include('world.urls')),

    # UserOffers
    path('useroffer/', include('useroffer.urls')),
]
