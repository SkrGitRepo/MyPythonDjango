from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from blogs.views import blog_sitemap

sitemaps = {
    'blogs': blog_sitemap
}
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blogs.views.index', name='home'),
    url(r'^blogs/$', 'blogs.views.blogs', name='blogs'),
    url(r'^blogs/(?P<slug>[\w-]+)/$', 'blogs.views.blog_view', name='blog_view'),
    url(r'^blogs-category/(?P<slug>[\w-]+)/$', 'blogs.views.category_view', name='category_view'),
    url(r'^contact/$', 'blogs.views.contact', name='contact'),
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow:", content_type="text/plain")),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    #(r'^ckeditor/', include('ckeditor.urls')),
    (r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^kdadmin/', include(admin.site.urls)),
)

urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))
urlpatterns += patterns('', (
    r'^media/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}
))
handler404 = 'blogs.views.handler404'

handler500 = 'blogs.views.handler500'