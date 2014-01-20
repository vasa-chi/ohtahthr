from django.conf.urls import patterns, url
from views import TagFeed, SearchByTag

urls = patterns("",
    url(r"^gettags/$", name="get_tags", view=TagFeed.as_view()),
    url(r"^search/bytag/$", name="search_by_tag", view=SearchByTag.as_view())
)