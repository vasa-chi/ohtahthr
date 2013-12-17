# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from ohthathr.views import BaseCreateView
from models import UserFeedback
from forms import FeedbackForm
from api import create_feedback


class FeedbackCreateView(BaseCreateView):
    model = UserFeedback
    template_name = "create_feedback.html"
    form_class = FeedbackForm

    def _get_api_function(self):
        return create_feedback

    def prepare_api_data(self, form_cleaned_data):
        data = super(FeedbackCreateView, self).prepare_api_data(form_cleaned_data)
        from django.contrib.auth.models import User
        data["user"] = User.objects.get(pk=1)  # self.request.user TODO: remove placeholder
        if "objtype" in self.kwargs:
            data["objtype"] = int(self.kwargs["objtype"])
            data["pk"] = self.kwargs["pk"]
        return data

    def get_form_kwargs(self):
        kwargs = super(FeedbackCreateView, self).get_form_kwargs()
        user = self.request.user
        kwargs["email"] = user.email if not user.is_anonymous() else None
        return kwargs

    def get_success_url(self):
        return reverse("index")