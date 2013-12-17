# -*- coding: utf-8 -*-
from ohthathr.forms import BaseForm
from models import UserFeedback


class FeedbackForm(BaseForm):

    def __init__(self, *args, **kwargs):
        email = kwargs.pop("email")
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields["email"].initial = email
        self.fields.pop("tags")

    class Meta:
        fields = ("type", "email", "text")
        model = UserFeedback