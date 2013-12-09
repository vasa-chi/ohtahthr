# -*- coding: utf-8 -*-
from django.db.models import F
from taggit.models import Tag

#TODO: last_edit date will be updated on UPDATE call?


def inc_rating(pk, model):
    model.objects.select_for_update().get(pk=pk).update(rating=F("rating") + 1)
    #TODO: notify


def dec_ration(pk, model):
    model.objects.select_for_update().get(pk=pk).update(rating=F("rating") - 1)
    #TODO: notify


def get_tags(tag_names):
    tags = []
    for tag_name in tag_names:
        qs = Tag.objects.filter(name__exact=tag_name)
        if qs.exists():
            tags.append(qs[0])
        else:
            tags.append(Tag.objects.create(name=tag_name))
    return tags