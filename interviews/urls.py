# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import InterviewListView, InterviewDetailView, InterviewCreateView

urls = patterns("",
    url(r"^onfuji/list/$", name="on_fuji_list", view=InterviewListView.as_view()),
    url(r"^onfuji/create/$", name="on_fuji_create", view=InterviewCreateView.as_view()),
    url(r"^onfuji/(?P<pk>\d+)/$", name="fuji_detail", view=InterviewDetailView.as_view())
)