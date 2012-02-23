from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from myapp.api.tools import v1_api

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
    (r'^tastytools/', include('tastytools.urls'), {'api_name': v1_api.api_name}),
)
