# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import RatingView

urls = patterns("",
    url(r"^rate/$", name="rate", view=RatingView.as_view()),
)