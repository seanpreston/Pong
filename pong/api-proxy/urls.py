from django.conf.urls import patterns, url

urlpatterns = patterns('pong.api-proxy.views',
    # Registration URLs
    url(r'^(?P<path>.*)$', 'proxy', name='api-proxy'),
)
