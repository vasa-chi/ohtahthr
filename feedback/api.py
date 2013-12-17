# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from models import UserFeedback
from ohthathr.api import TYPE_MATCH_MAP


def create_feedback(data):
    """Создает отзыв.
       Опционально можно передать объект, что бы создать фидбек
       для чего-то(коммент, вакансия, интервью)
       Args:
            data: словарь с данным для создания фидбека.
                  Ключи :
                         objtype: Тип объекта. См. TYPE_MATCH_MAP
                         pk: PK объекта, число.
                         text: Текст сообщения.
                         email: email пользователя
                         user: пользователь, оставивший отзыв
                         type: тип отзыва, см. UserFeedback.TYPE_CHOICES
       Raises: Http404 если объект не найден

          """
    object = None
    if "objtype" in data and "pk" in data:
        model = TYPE_MATCH_MAP[data["objtype"]]
        object = get_object_or_404(model, pk=data["pk"])
    if object:
        data["object"] = object
    fb = UserFeedback.objects.create(**data)
    return fb