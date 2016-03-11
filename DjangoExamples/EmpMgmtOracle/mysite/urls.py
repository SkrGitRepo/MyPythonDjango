"""mysite URL Configuration

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
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.conf import settings
from django.conf.urls.static import static




from mysite.EmpMgmtApp.models import Emp

admin.autodiscover()
#info_dict = {
#             'queryset':Emp.objects.all(),
#}

employee_info = {'model' : Emp}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^empmgmt$','mysite.EmpMgmtApp.views.login'),
    url(r'^empmgmt/contact$','mysite.EmpMgmtApp.views.contactus'),
    url(r'^accounts/auth/$','mysite.EmpMgmtApp.views.auth_view'),
    url(r'^accounts/logout/$','mysite.EmpMgmtApp.views.logout'),
    url(r'^accounts/invalid/$','mysite.EmpMgmtApp.views.invalid_login'),
    #url(r'^empmgmt$', 'mysite.EmpMgmtApp.views.home', name='home'),
    #url(r'^employees/$', 'django.views.generic.list.ListView',dict(info_dict, template_name='employee_list.html')),
    #url(r'^employees/$',ListView.as_view(queryset=Emp.objects.all,paginate_by=5,template_name='employee_list.html')),
    url(r'^employees/$',ListView.as_view(queryset=Emp.objects.all,template_name='employee_list.html')),
    #url(r'^employees/$', 'django.views.generic.list.ListView',dict(info_dict, TemplateView.as_view(template_name='employees/employee_list.html'))),
    url(r'^employees/create/$',CreateView.as_view(model=Emp,fields=['empno','ename','job','mgr','hiredate','sal','comm','deptno'],template_name='employee_form.html',success_url='/employees')),
    #url(r'^employees/update/(?P<object_id>\d+)/$', 'django.views.generic.edit.UpdateView',
#dict(employee_info, template_name='employees/employee_form.html', post_save_redirect='/employees/')),
    url(r'^employees/update/(?P<pk>\d+)/$', UpdateView.as_view(model=Emp,fields=['empno','ename','job','mgr','hiredate','sal','comm','deptno'],template_name='employee_form.html',success_url='/employees')),
    url(r'^employees/delete/(?P<pk>\d+)/$', DeleteView.as_view(model=Emp,template_name='employee_confirm_delete.html',success_url='/employees')),
    #url(r'^employees/delete/(?P<object_id>\d+)/$', 'django.views.generic.edit.DeleteView',
#dict(employee_info, template_name='employees/employee_confirm_delete.html',post_delete_redirect='/employees/')),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': 'C:/DjangoPythonWorkSpace/EmpMgmtOracle/mysite/EmpMgmtApp/static'}),
    #url(r'^mysite/', include('mysite.foo.urls')),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL,
#                          document_root=settings.STATIC_ROOT)
#    urlpatterns += static(settings.MEDIA_URL,
#                          document_root=settings.MEDIA_ROOT)