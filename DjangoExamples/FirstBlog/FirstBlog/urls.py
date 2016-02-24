"""FirstBlog URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^contact$', 'blog.views.contact', name='contact'),
    url(r'^viewblog$', 'blog.views.viewblog', name='viewblog'),
    url(r'^addblog$', 'blog.views.submitBlog', name='submitBlog'),
    url(r'^saveblog/$', 'blog.views.saveBlog', name='saveBlog'),
    url(r'^signup$', 'blog.views.signup', name='signup'),
    url(r'^saveuser/$', 'blog.views.saveUser', name='saveUser'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
      
    
