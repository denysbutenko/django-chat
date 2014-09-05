# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from socketio import sdjango

sdjango.autodiscover()

urlpatterns = patterns(
    "chat.views",
    url("^socket\.io", include(sdjango.urls)),
)