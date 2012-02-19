from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from myapp.api.resources import EntryResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EntryResource())

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)
