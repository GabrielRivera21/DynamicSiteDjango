from django.conf.urls import patterns, url

from . import views

urlpatterns = [
    url(
        r'^$',
        views.HomeView.as_view(),
        name="home"
    ),
    url(
        r'about',
        views.AboutUsView.as_view(),
        name="about"
    ),
]
