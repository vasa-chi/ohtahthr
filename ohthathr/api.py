# -*- coding: utf-8 -*-
from django.db.models import F
from taggit.models import Tag
from models import Company

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
        tags.append(Tag.objects.get_or_create(name__iexact=tag_name))
    return tags


def get_company(company_name):
    qs = Company.objects.filter(title__iexact=company_name)
    if qs.exists():
        return qs[0]
    else:
        return Company.objects.create(title=company_name)