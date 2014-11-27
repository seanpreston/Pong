from django.conf.urls import patterns, url

urlpatterns = patterns('pong.registration.views',

    # Registration URLs
    url(r'^registration/$', 'index', name='registration-index'),
    url(r'^registration/user/$', 'register_user', name='registration-user'),

)
