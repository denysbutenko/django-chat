# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from socketio import sdjango

sdjango.autodiscover()

urlpatterns = patterns(
    "apps.chat.views",
    url(r'^$', "index"),
    url("^create_channel/$", "create_channel", name="create_channel"),
    url("^(?P<slug>.*)$", "channel", name="channel"),
    url("^socket\.io", include(sdjango.urls)),
)
