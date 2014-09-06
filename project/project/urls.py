from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url("", include("apps.chat.urls")),

    # Auth
    url(r'^signin/$', 'apps.users.views.signin_view', name="signin"),
    url(r'^signup/$', 'apps.users.views.signup_view', name="signup"),
    url(r'^signout/$', 'apps.users.views.signout_view', name="signout"),
)
