# -*- coding: utf-8 -*-
from models import Interview
from ohthathr.api import get_tags, get_company
from django.http import Http404


def create_interview(data):
    """Создает инстанс interviews.models.Interview.
       Args:
            data - словарь с данными для создания.
       Returns:
            Созданный инстанс модели interviews.models.Interview.
    """
    i = Interview.objects.create(title=data["title"],
                                 url=data["url"],
                                 added_by=data["user"],
                                 description=data["description"],
                                 was_success=data["was_success"],
                                 company=get_company(data["company"]))
    i.tags = get_tags(data["tags"])
    return i


def update_interview(interview_pk, user, changed_data):
    """Обновляет инстанс interviews.models.Interview.
       Args:
            interview_pk - pk для запроса. Число.
            user - инстанс модели пользователя. Для фильтра.
            changed_data - словарь с измененными данными.
       Raises:
              Http404 - если интервью не найдено.
    """
    try:
        interview = (Interview.objects
                     .select_for_update()
                     .get(pk=interview_pk, added_by=user))
    except Interview.DoesNotExist:
        raise Http404()
    else:
        if "tags" in changed_data:
            interview.tags = get_tags(changed_data.pop("tags"))
        if "company" in changed_data:
            changed_data["company"] = get_company(changed_data["company"])
        interview.update(**changed_data)
        #TODO: notify


def delete_interview(interview_pk, user):
    """Удаление интервью.
       Args:
            interview_pk - pk для запроса. Число.
            user - инстанс модели пользователя. Для фильтра.
       Raises:
            Http404 - если интервью не найдено.
    """
    try:
        (Interview.objects
         .select_for_update()
         .filter(pk=interview_pk, added_by=user)
         .update(deleted=True))
        #TODO:  schedule to delete
    except Interview.DoesNotExist:
        raise Http404()
    # TODO: clear notify