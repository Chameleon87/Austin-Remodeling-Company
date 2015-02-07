from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ar.views.index'),
    url(r'^commercial', 'ar.views.commercial'),
    url(r'^residential', 'ar.views.residential'),
    url(r'^hometheatre', 'ar.views.hometheatre'),
    url(r'^ssf', 'ar.views.ssf'),
    url(r'^contact', 'ar.views.contact'),
    url(r'^thankyou', 'ar.views.thankyou'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
