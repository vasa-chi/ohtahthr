# -*- coding: utf-8 -*-
from django.forms import ModelForm
from taggit.forms import TagField


class BaseForm(ModelForm):

    tags = TagField(label=u"Теги", help_text=u"От 1 до 10 тегов. Название компании, технологии или ощущения")

    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs["class"] = field.widget.attrs.get("class", "") + " form-control"
            if name == "tags":
                field.widget.input_type = "hidden"