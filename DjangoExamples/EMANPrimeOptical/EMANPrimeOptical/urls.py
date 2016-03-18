from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'EMANPrimeOptical.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^prime/optical$', 'EMANPrimeOptical.UserProvReporter.views.home', name='home'),
    #url(r'^prime/optical/cpo-prod-superuser$', 'EMANPrimeOptical.UserProvReporter.views.cpo_prod_superuser', name='cpo_prod_superuser'),
    url(r'^prime/optical/cpo-(\w+)-(\w+)/$', 'EMANPrimeOptical.UserProvReporter.views.find_cpo_users', name='find_cpo_users'),
    #url(r'^prime/optical/(\w+)/(\d+)/$', 'EMANPrimeOptical.UserProvReporter.views.find_cpo_user', name='find_cpo_user'),
    #url(r'^prime/optical/cpo-prod-sysadmin$', 'EMANPrimeOptical.UserProvReporter.views.cpo_prod_sysadmin', name='cpo_prod_sysadmin'),
    #url(r'^prime/optical/cpo-prod-networkadmin$', 'EMANPrimeOptical.UserProvReporter.views.cpo_prod_networkadmin', name='cpo_prod_networkadmin'),
    #url(r'^prime/optical/cpo-prod-operator$', 'EMANPrimeOptical.UserProvReporter.views.cpo_prod_operator', name='cpo_prod_operator'),
    #url(r'^prime/optical/cpo-prod-provisioner$', 'EMANPrimeOptical.UserProvReporter.views.cpo_prod_provisioner', name='cpo_prod_provisioner'),
    url(r'^prime/optical/search/user$','EMANPrimeOptical.UserProvReporter.views.search_user',name='search_user'),
    #url(r'^prime/optical/search/user/(?P<userid>[-\w]+)/(?P<userrole>\w+)/$','EMANPrimeOptical.UserProvReporter.views.search_user',name='search_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)