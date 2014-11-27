# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.auth.views import logout_then_login

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_settings.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),

    # API Proxy
    url(r'^site-api-(?P<api>0|1|public|public-1)/', include('pong.api-proxy.urls')),

    # API v0
    url(r'^', include('pong.api_urls')),

    # Dash
    url(r'^dash/$', 'pong.views.dash', name='dash'),

    # Login
    url(r'^login/$', 'pong.views.login', name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),

    # Registration
    url(r'^', include('pong.registration.urls')),

    # Landing
    url(r'^$', 'pong.views.landing', name='landing'),

)
# ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
