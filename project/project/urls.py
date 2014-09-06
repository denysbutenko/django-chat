from django.views.generic.base import RedirectView
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Main page
    url(r'^$', RedirectView.as_view(url="/channels/")),

    # Apps
    url("", include("apps.chat.urls", namespace="chat")),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Auth
    url(r'^signin/$', 'apps.users.views.signin_view', name="signin"),
    url(r'^signup/$', 'apps.users.views.signup_view', name="signup"),
    url(r'^signout/$', 'apps.users.views.signout_view', name="signout"),
)
