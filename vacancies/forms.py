# -*- coding: utf-8 -*-
from models import Vacancy
from ohthathr.forms import BaseForm


class VacancyForm(BaseForm):

    class Meta:
        model = Vacancy
        fields = ("title", "url", "description", "why")