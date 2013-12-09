# -*- coding: utf-8 -*-
from ohthathr.views import BaseListView, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView
from models import Interview
from forms import InterviewForm
from api import create_interview, delete_interview, update_interview


class InterviewListView(BaseListView):
    template_name = "interview_list.html"
    model = Interview


class InterviewDetailView(BaseDetailView):
    model = Interview
    template_name = "interview_detail.html"


class InterviewCreateView(BaseCreateView):
    template_name = "interview_create.html"
    form_class = InterviewForm
    success_url = "interview_detail"
    model = Interview

    def prepare_api_data(self, form_cleaned_data):
        from django.contrib.auth.models import User  # placeholder
        form_cleaned_data["added_by"] = User.objects.get(pk=1)  # self.request.user
        return super(InterviewCreateView, self).prepare_api_data(form_cleaned_data)

    def _get_api_function(self):
        return create_interview


class InterviewUpdateView(BaseUpdateView):
    template_name = "interview_edit.html"
    form_class = InterviewForm
    success_url = "interview_detail"
    model = Interview

    def _get_api_function(self):
        return update_interview


class InterviewDeleteView(BaseDeleteView):
    template_name = "interview_delete.html"
    success_url = "interview_list"
    model = Interview

    def _get_api_function(self):
        return delete_interview