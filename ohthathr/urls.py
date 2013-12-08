from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from interviews.urls import urls as interviews_urls
admin.autodiscover()

urlpatterns = patterns("",
    # Examples:
    # url(r'^$', 'ohthathr.views.home', name='home'),

    url(r"^admin/", include(admin.site.urls)),

    #url('', include('social.apps.django_app.urls', namespace='social'))
    url(r"^$", name="index", view=TemplateView.as_view(template_name="base.html")),
)
urlpatterns += interviews_urls