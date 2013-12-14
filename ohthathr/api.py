# -*- coding: utf-8 -*-
from taggit.models import Tag
from interviews.models import Interview
from vacancies.models import Vacancy

TYPE_MATCH_MAP = {
    0: Vacancy,
    1: Interview
}


def get_tags(tag_names):
    tags = []
    for tag_name in tag_names:
        qs = Tag.objects.filter(name__exact=tag_name)
        if qs.exists():
            tags.append(qs[0])
        else:
            tags.append(Tag.objects.create(name=tag_name))
    return tags