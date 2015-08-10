from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(
        r'^admin/',
        include(admin.site.urls)
    ),
    url(
        r'^',
        include('brics.home.urls')
    ),
    url(
        r'^',
        include('brics.contact.urls')
    ),
    url(
        r'^',
        include('brics.services.urls')
    ),
]


if settings.ENVIRONMENT == 'DEVELOPMENT':
    urlpatterns = urlpatterns +\
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
