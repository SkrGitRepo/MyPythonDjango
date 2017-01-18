from django.conf.urls import include, url
from django.contrib import admin
from AuthTestApp import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'LoginApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home, name='home'),
]
