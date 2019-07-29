from django.conf.urls import include, url

urlpatterns = [
    url(r'^index/', include('apps.index.urls')),
    url(r'^upload/', include('apps.web.urls')),
    url(r'^websock/', include('apps.websock.urls')),
]
