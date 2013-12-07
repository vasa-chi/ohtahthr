# -*- coding: utf-8 -*-
from models import Vacancy
from ohthathr.api import get_tags, get_company
from django.http import Http404


def create_vacancy(data):
    """Создает инстанс vacancies.models.Vacancy.
       Args:
            data - словарь с данными для создания.
       Returns:
            Созданный инстанс модели vacancies.models.Vacancy.
    """
    v = Vacancy.objects.create(type=data["type"],
                               title=data["title"],
                               url=data["url"],
                               added_by=data["user"],
                               description=data["description"],
                               why=data["why"],
                               company=get_company(data["company"])
                               )
    v.tags = get_tags(data["tags"])
    return v


def update_vacancy(vacancy_pk, user, changed_data):
    """Обновляет инстанс vacancies.models.Vacancy.
       Args:
            vacancy_pk - pk для запроса. Число.
            user - инстанс модели пользователя. Для фильтра.
            changed_data - словарь с измененными данными.
       Raises:
              Http404 - если вакансия не найдена.
    """
    try:
        vacancy = (Vacancy.objects
                   .select_for_update()
                   .get(pk=vacancy_pk, added_by=user))
    except Vacancy.DoesNotExist:
        raise Http404()
    else:
        if "tags" in changed_data:
            vacancy.tags = get_tags(changed_data.pop("tags"))
        if "url" in changed_data:
            pass  # TODO: generate another content?
        if "company" in changed_data:
            changed_data["company"] = get_company(changed_data["company"])
        vacancy.update(**changed_data)
        #TODO: notify


def delete_vacancy(vacancy_pk, user):
    """Удаление интервью.
       Args:
            vacancy_pk - pk для запроса. Число.
            user - инстанс модели пользователя. Для фильтра.
       Raises:
            Http404 - если вакансия не найдена.
    """
    try:
        (Vacancy
         .objects.select_for_update()
         .filter(pk=vacancy_pk, added_by=user)
         .update(deleted=True))
        #TODO:  schedule to delete
    except Vacancy.DoesNotExist:
        raise Http404()
    # TODO: clear notify