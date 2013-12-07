# -*- coding: utf-8 -*-
from models import Vacancy
from ohthathr.api import get_tags
from django.http import Http404


def create_vacancy(data):
    company = ""  # data["company"]
    v = Vacancy.objects.create(type=1,
                               title=data["title"],
                               url=data["url"],
                               added_by=data["user"],
                               description=data["description"],
                               why=data["why"],
                               company=company
                               )
    v.tags = get_tags(data["tags"])
    return v


def update_vacancy(vacancy_pk, user, changed_data):
    try:
        vacancy = Vacancy.objects.select_for_update().get(pk=vacancy_pk, added_by=user)
    except Vacancy.DoesNotExist:
        raise Http404()
    else:
        if "tags" in changed_data:
            vacancy.tags = get_tags(changed_data["tags"])
        if "url" in changed_data:
            pass  # TODO: generate another content?
        vacancy.update(**changed_data)
        #TODO: notify


def delete_vacancy(vacancy_pk, user):
    try:
        (Vacancy.objects.select_for_update()
         .get_(pk=vacancy_pk, added_by=user)
         .update(deleted=False))
        #TODO:  schedule to delete
    except Vacancy.DoesNotExist:
        raise Http404()
    # TODO: clear notify