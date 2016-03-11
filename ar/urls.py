from django.conf.urls import patterns, include, url
from django.contrib import admin
from ar.views import index, commercial, residential, hometheatre, ssf, contact, thankyou
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index),
    url(r'^commercial', commercial),
    url(r'^residential', residential),
    url(r'^hometheatre', hometheatre),
    url(r'^ssf', ssf),
    url(r'^contact', contact),
    url(r'^thankyou', thankyou),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
