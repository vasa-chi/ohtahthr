# -*- coding: utf-8 -*-
from models import Interview
from ohthathr.api import get_tags


def create_interview(data):
    """Создает инстанс interviews.models.Interview.
       Args:
            data - словарь с данными для создания.
       Returns:
            Созданный инстанс модели interviews.models.Interview.
    """
    i = Interview.objects.create(title=data["title"],
                                 url=data["url"],
                                 added_by=data["added_by"],
                                 description=data["description"],
                                 was_success=data["was_success"])
    i.tags = get_tags(data["tags"])
    return i


def update_interview(interview, changed_data):
    """Обновляет инстанс interviews.models.Interview.
       Args:
            interview - инстанс interview.models.Interview.
            changed_data - словарь с измененными данными.
    """
    if "tags" in changed_data:
        interview.tags = get_tags(changed_data.pop("tags"))
    Interview.objects.filter(pk=interview.pk).update(**changed_data)
    #TODO: notify


def delete_interview(interview):
    """Удаление интервью.
       Args:
            interview - инстанс interview.models.Interview.
    """
    Interview.objects.filter(pk=interview.pk).update(deleted=True)
    # TODO:  schedule to delete
    # TODO: clear notify