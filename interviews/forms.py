# -*- coding: utf-8 -*-
from models import Interview
from ohthathr.forms import BaseForm


class InterviewForm(BaseForm):

    class Meta:
        model = Interview
        fields = ("title", "url", "description", "was_success", "tags")