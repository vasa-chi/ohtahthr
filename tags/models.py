# -*- coding: utf-8 -*-
from django.db import models
from taggit.models import TagBase, GenericTaggedItemBase


class CountedTag(TagBase):

    count = models.PositiveIntegerField(verbose_name=u"кол-во использований", default=1)

    class Meta:
        ordering = ["count"]


class CountedTagThrough(GenericTaggedItemBase):
    tag = models.ForeignKey(CountedTag,
                            related_name="%(app_label)s_%(class)s_items")