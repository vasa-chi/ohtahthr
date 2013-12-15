from django.conf.urls import patterns, url
from views import TagFeed

urlpatterns = patterns("",
    url(r"^gettags$", name="get_tags", view=TagFeed.as_view()),
)