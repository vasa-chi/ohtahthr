# -*- coding: utf-8 -*-
from models import Vacancy


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
                               added_by=data["added_by"],
                               description=data["description"],
                               why=data["why"]
                               )
    v.tags.add(*data["tags"])
    return v


def update_vacancy(vacancy, changed_data):
    """Обновляет инстанс vacancies.models.Vacancy.
       Args:
            vacancy - инстанс вакансии. vacancies.models.Vacancy.
            changed_data - словарь с измененными данными.
    """
    if "tags" in changed_data:
        vacancy.tags.clear()
        vacancy.tags.add(*changed_data.pop("tags"))
    if "url" in changed_data:
        pass  # TODO: generate another content?
    Vacancy.objects.select_for_update().filter(pk=vacancy.pk).update(**changed_data)
    #TODO: notify


def delete_vacancy(vacancy):
    """Удаление интервью.
       Args:
            vacancy - инстанс вакансии. vacancies.models.Vacancy.
    """
    Vacancy.objects.select_for_update().filter(pk=vacancy.pk).update(deleted=True)
    # TODO: schedule to delete
    # TODO: clear notify