# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import CommentCreateView, CommentDeleteView, CommentUpdateView

urls = patterns("",
    url(r"^comments/add/$", name="comment_add", view=CommentCreateView.as_view()),
    url(r"^comments/edit/$", name="comment_edit", view=CommentUpdateView.as_view()),
)