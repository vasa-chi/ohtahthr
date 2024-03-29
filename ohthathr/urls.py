from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from interviews.urls import urls as interviews_urls
from vacancies.urls import urls as vacancies_urls
from comments.urls import urls as comments_urls
from rating.urls import urls as rating_urls
from tags.urls import urls as tags_urls
from feedback.urls import urls as feeback_urls
from views import SearchView
admin.autodiscover()

urlpatterns = patterns("",

    url(r"^admin/", include(admin.site.urls)),
    #url('', include('social.apps.django_app.urls', namespace='social'))
    url(r"^$", name="index", view=TemplateView.as_view(template_name="base.html")),
    url(r"^search/$", name="search", view=SearchView.as_view())
)
urlpatterns += interviews_urls
urlpatterns += vacancies_urls
urlpatterns += comments_urls
urlpatterns += rating_urls
urlpatterns += tags_urls
urlpatterns += feeback_urls