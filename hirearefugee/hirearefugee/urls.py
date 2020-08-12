from django.conf import settings
from django.conf.urls.static import static

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

    # UserClass
    path('userclass/', include('userclass.urls')),

    # UserOffers
    path('useroffer/', include('useroffer.urls')),
]

# Make url for media automatically
if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)