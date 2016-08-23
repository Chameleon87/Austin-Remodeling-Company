from django.conf.urls import include, url
from django.contrib import admin
from ar.views import index, commercial, residential, hometheatre, ssf, contact, thankyou
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', index, name="/"),
    url(r'^index/$', index, name="index"),
    url(r'^commercial/', commercial, name="commercial"),
    url(r'^residential/', residential, name="residential"),
    url(r'^hometheatre/', hometheatre, name="hometheatre"),
    url(r'^ssf/', ssf, name="ssf"),
    url(r'^contact/', contact, name="contact"),
    url(r'^thankyou/', thankyou, name="thankyou"),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
