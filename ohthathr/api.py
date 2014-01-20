# -*- coding: utf-8 -*-
from interviews.models import Interview
from vacancies.models import Vacancy
from comments.models import Comment
from django.db.models import Q
from django.template.defaultfilters import date
from itertools import chain

TYPE_MATCH_MAP = {
    0: Vacancy,
    1: Interview,
    2: Comment
}

TYPE_MATCH_REVERSE = {
    Vacancy: 0,
    Interview: 1,
    Comment: 2
}


def search(term, only_by_tag=False):
    """ Возвращает результаты поиска по основным разделам ввиде json-массива.
        Args:
            term - Искомое. Строка.
        Returns:
            Список (list) объектов(вакансии + интервью - в таком порядке)
            отсортированных по дате добавления.
            Объект списка - словарь:
                data:
                    title: Заголовок записи. Строка.
                    added_by: Кем добавлена запись. Строка.
                    description: Описание записи. Строка.
                    date: Дата добавления записи.
                          Дата строкой в формате dd.mm.yyyy hh:mm:ss.
                    url: Внешний url. См. ohthathr.models.Base.url.
                    rating: Рейтинг.
                    tags: Теги для записи.

                    Только для вакансий:
                        why: Почему добавлена вакансия.
                             Cм. vacancies.models.Vacancy.why.
                        type: Тип вакансии.
                              См. vacancies.models.Vacancy.VACANCY_TYPE_CHOICES.
                type: Тип записи - вакансия или интервью.
                      См. TYPE_MATCH_MAP/TYPE_MATCH_REVERSE выше.

    """
    results = []
    if not only_by_tag:
        tag_q = Q(tags__name__icontains=term)
        title_q = Q(title__icontains=term)
        description_q = Q(description__icontains=term)
        why_q = Q(why__icontains=term)  # only for vacancies and only for convince
    else:
        tag_q = Q(tags__name=term)
        title_q = Q()
        description_q = Q()
        why_q = Q()  # only for vacancies and only for convince
    vacancies = list(Vacancy.objects.filter(title_q | description_q | why_q | tag_q)
                                    .order_by("date", "pk")
                                    .select_related("added_by")
                                    .prefetch_related('tagged_items__tag')
                                    .distinct("date", "pk"))
    interviews = list(Interview.objects.filter(title_q | description_q | tag_q)
                                       .order_by("date", "pk")
                                       .select_related("added_by")
                                       .prefetch_related('tagged_items__tag')
                                       .distinct("date", "pk"))
    for obj in chain(vacancies, interviews):
        data = {"data": {"title": obj.title,
                         "added_by": unicode(obj.added_by),  # TODO: user formatting - url, etc.
                         "description": obj.description,
                         "date": date(obj.date, "d.m.Y H:i:s"),
                         "url": obj.url,
                         "rating": obj.rating,
                         "tags": [tag.name for tag in obj.tags.all()]},
                "type": TYPE_MATCH_REVERSE[obj.__class__]
                }
        if isinstance(obj, Vacancy):
            data["data"]["why"] = obj.why
            data["data"]["type"] = obj.type
        results.append(data)
    return results