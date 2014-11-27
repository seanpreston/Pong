# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    '',

    # URLs

    # Account
    url(r'^', include('pong.account.api_urls')),

    # Registration
    url(r'^', include('pong.registration.api_urls')),

)
