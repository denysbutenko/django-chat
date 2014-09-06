# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from socketio import sdjango

sdjango.autodiscover()

urlpatterns = patterns(
    "apps.chat.views",
    url("^socket\.io", include(sdjango.urls)),

    url(r'^channels/$', "index"),
    url(r'^create_channel/$', "create_channel", name="create_channel"),
    url(r'^channel/(?P<slug>.*)/$', "channel", name="channel"),
)
