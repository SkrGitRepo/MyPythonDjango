"""A2ZShopeeOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^a2zshop$', 'A2ZShop.views.home', name='home'),
    url(r'^women$', 'A2ZShop.views.womenshop', name='womenshop'),
    url(r'^register$', 'A2ZShop.views.registration', name='registration'),
    url(r'^checkout$', 'A2ZShop.views.checkout', name='checkout'),
    url(r'^details$', 'A2ZShop.views.prodetails', name='prodetails'),
    url(r'^contact$', 'A2ZShop.views.contactdetails', name='contactdetails'),
    #url(r'^$', 'A2ZShop.views.home', name='home'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)