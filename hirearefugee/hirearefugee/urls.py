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
from django.urls import path
from useroffer import views as useroffer_views
from support import views as support_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', useroffer_views.signupuser, name='signupuser'),
    path('login/', useroffer_views.loginuser, name='loginuser'),
    path('logout/', useroffer_views.logoutuser, name='logoutuser'),

    # Support
    path('support/becomeamember', support_views.becomeamember, name='becomeamember'),
    path('support/donate', support_views.donate, name='donate'),
    path('support/helpcoding', support_views.helpcoding, name='helpcoding'),
    path('support/sponsors', support_views.sponsors, name='sponsors'),
    path('support/spreadtheword', support_views.spreadtheword, name='spreadtheword'),
    path('support/thanks', support_views.thanks, name='thanks'),

    # Navbar
    path('about/', useroffer_views.about, name='about'),
    path('testhtml/', useroffer_views.testhtml, name='testhtml'),

    # UserOffers
    path('', useroffer_views.home, name='home'),
    path('create/', useroffer_views.createuseroffer, name='createuseroffer'),
    path('current/', useroffer_views.currentuseroffers, name='currentuseroffers'),
    path('completed/', useroffer_views.completeduseroffers, name='completeduseroffers'),
    path('useroffer/<int:useroffer_pk>', useroffer_views.viewuseroffer, name='viewuseroffer'),
    path('useroffer/<int:useroffer_pk>/complete', useroffer_views.completeuseroffer, name='completeuseroffer'),
    path('useroffer/<int:useroffer_pk>/delete', useroffer_views.deleteuseroffer, name='deleteuseroffer'),
]
