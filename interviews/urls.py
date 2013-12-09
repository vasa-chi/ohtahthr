# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import InterviewListView, InterviewDetailView, InterviewCreateView, InterviewUpdateView, InterviewDeleteView

urls = patterns("",
    url(r"^interviews/$", name="interview_list", view=InterviewListView.as_view()),
    url(r"^interviews/create/$", name="interview_create", view=InterviewCreateView.as_view()),
    url(r"^interview/(?P<pk>\d+)/edit/$", name="interview_edit", view=InterviewUpdateView.as_view()),
    url(r"^interview/(?P<pk>\d+)/delete/$", name="interview_delete", view=InterviewDeleteView.as_view()),
    url(r"^interview/(?P<pk>\d+)/$", name="interview_detail", view=InterviewDetailView.as_view())
)