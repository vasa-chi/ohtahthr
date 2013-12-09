# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import (WatVacancyCreateView, WatVacancyListView, VacancyDeleteView, VacancyDetailView,
                   VacancyUpdateView, DreamVacancyCreateView, DreamVacancyListView)

urls = patterns("",
    url(r"^watparade/$", name="wat_parade", view=WatVacancyListView.as_view()),
    url(r"^watparade/create/$", name="wat_parade_create", view=WatVacancyCreateView.as_view()),
    url(r"^dreamparade/$", name="dream_parade", view=DreamVacancyListView.as_view()),
    url(r"^dreamparade/create/$", name="dream_parade_create", view=DreamVacancyCreateView.as_view()),
    url(r"^vacancy/(?P<pk>\d+)/edit/$", name="vacancy_edit", view=VacancyUpdateView.as_view()),
    url(r"^vacancy/(?P<pk>\d+)/delete/$", name="vacancy_delete", view=VacancyDeleteView.as_view()),
    url(r"^vacancy/(?P<pk>\d+)/$", name="vacancy_detail", view=VacancyDetailView.as_view()),

)