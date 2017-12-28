from django.conf.urls import include, url, patterns

urlpatterns = patterns('',
    url(r'^index/', include('apps.index.urls')),
    url(r'^upload/', include('apps.web.urls')),
)
