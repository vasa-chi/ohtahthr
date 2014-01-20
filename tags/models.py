# -*- coding: utf-8 -*-
from django.db import models
from taggit.models import TagBase, GenericTaggedItemBase
from django.core.urlresolvers import reverse


class CountedTag(TagBase):

    count = models.PositiveIntegerField(verbose_name=u"кол-во использований", default=1)

    class Meta:
        ordering = ["count"]

    def get_absolute_url(self):
        return u"{0}?q={1}".format(reverse("search_by_tag"), self.name)


class CountedTagThrough(GenericTaggedItemBase):
    tag = models.ForeignKey(CountedTag,
                            related_name="%(app_label)s_%(class)s_items")