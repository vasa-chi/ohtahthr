from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ohthathr.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),

    #url('', include('social.apps.django_app.urls', namespace='social'))
)


