# -*- coding: utf-8 -*-
from django.forms import ModelForm


class BaseForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = field.widget.attrs.get("class", "") + " form-control"