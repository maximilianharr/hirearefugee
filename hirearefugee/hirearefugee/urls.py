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
from home import views as home_views
from support import views as support_views
from userauth import views as userauth_views
from useroffer import views as useroffer_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('userauth/signup/', userauth_views.signupuser, name='signupuser'),
    path('userauth/login/', userauth_views.loginuser, name='loginuser'),
    path('userauth/logout/', userauth_views.logoutuser, name='logoutuser'),

    # Support
    path('support/becomeamember', support_views.becomeamember, name='becomeamember'),
    path('support/donate', support_views.donate, name='donate'),
    path('support/helpcoding', support_views.helpcoding, name='helpcoding'),
    path('support/sponsors', support_views.sponsors, name='sponsors'),
    path('support/spreadtheword', support_views.spreadtheword, name='spreadtheword'),
    path('support/thanks', support_views.thanks, name='thanks'),

    # Home
    path('', home_views.home, name='home'),
    path('home/', home_views.home, name='home'),
    path('home/about/', home_views.about, name='about'),
    path('home/testhtml/', home_views.testhtml, name='testhtml'),

    # UserOffers
    path('create/', useroffer_views.createuseroffer, name='createuseroffer'),
    path('current/', useroffer_views.currentuseroffers, name='currentuseroffers'),
    path('completed/', useroffer_views.completeduseroffers, name='completeduseroffers'),
    path('useroffer/<int:useroffer_pk>', useroffer_views.viewuseroffer, name='viewuseroffer'),
    path('useroffer/<int:useroffer_pk>/complete', useroffer_views.completeuseroffer, name='completeuseroffer'),
    path('useroffer/<int:useroffer_pk>/delete', useroffer_views.deleteuseroffer, name='deleteuseroffer'),
]
