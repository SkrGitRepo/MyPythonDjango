from django.conf.urls import include, url
from django.contrib import admin
from RestApp import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'DjangoRestExample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    
]
