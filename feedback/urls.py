# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import FeedbackCreateView

urls = patterns("",
    url(r"^feedback/$", name="create_feedback", view=FeedbackCreateView.as_view()),
    url(r"^feedback/(?P<objtype>\d+)/(?P<pk>\d+)/$", name="create_feedback_for", view=FeedbackCreateView.as_view()),
)