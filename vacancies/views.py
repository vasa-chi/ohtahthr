# -*- coding: utf-8 -*-
from ohthathr.views import BaseListView, BaseCreateView, BaseDeleteView, BaseUpdateView, BaseDetailView
from models import Vacancy
from forms import VacancyForm
from api import create_vacancy, delete_vacancy, update_vacancy
from django.core.urlresolvers import reverse


class VacancyMixin(object):
    vacancy_type = None
    model = Vacancy

    def get_queryset(self):
        return super(VacancyMixin, self).get_queryset().filter(type=self.vacancy_type)

    def prepare_api_data(self, form_cleaned_data):
        form_cleaned_data = super(VacancyMixin, self).prepare_api_data(form_cleaned_data)

        from django.contrib.auth.models import User  # TODO: remove placeholder
        form_cleaned_data["added_by"] = User.objects.get(pk=1)  # self.request.user

        form_cleaned_data["type"] = self.vacancy_type
        return form_cleaned_data

    def get_context_data(self, **kwargs):
        context = super(VacancyMixin, self).get_context_data(**kwargs)
        context["vacancy_type"] = self.vacancy_type
        return context


class DreamVacancyListView(VacancyMixin, BaseListView):
    template_name = "dream_vacancy_list.html"
    vacancy_type = 3


class DreamVacancyCreateView(VacancyMixin, BaseCreateView):
    template_name = "vacancy/vacancy_create.html"
    form_class = VacancyForm
    vacancy_type = 3

    def _get_api_function(self):
        return create_vacancy

    def get_success_url(self):
        return reverse("dream_parade")


class WatVacancyListView(VacancyMixin, BaseListView):
    template_name = "wat_vacancy_list.html"
    vacancy_type = 1


class WatVacancyCreateView(DreamVacancyCreateView):
    success_url = "wat_parade"
    vacancy_type = 1

    def get_success_url(self):
        return reverse("wat_parade")


class VacancyDetailView(BaseDetailView):
    template_name = "vacancy/vacancy_detail.html"
    model = Vacancy


class VacancyUpdateView(BaseUpdateView):
    template_name = "vacancy/vacancy_edit.html"
    model = Vacancy
    form_class = VacancyForm

    def get_success_url(self):
        if self.object.type == 1:
            return reverse("wat_parade")
        elif self.object.type == 3:
            return reverse("dream_parade")

    def _get_api_function(self):
        return update_vacancy


class VacancyDeleteView(BaseDeleteView):
    template_name = "vacancy/vacancy_delete.html"
    model = Vacancy

    def get_success_url(self):
        if self.object.type == 1:
            return reverse("wat_parade")
        elif self.object.type == 3:
            return reverse("dream_parade")

    def _get_api_function(self):
        return delete_vacancy