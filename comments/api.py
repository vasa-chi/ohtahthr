# -*- coding: utf-8 -*-
from models import Comment
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from interviews.models import Interview
from vacancies.models import Vacancy

TYPE_MATCH_MAP = {
    "0": Vacancy,
    "1": Interview
}


def create_comment(data):
    """Создает комментарий для объекта object.
       Args:
            data: Словарь с данными для комментария.
            object: Объект, для кот. создается комментарий.

       Returns:
               Созданный инстанс комментария.

       Raises:
              Http404: если не найден родительский комментарий.
                       Так же, если не найдена запись для кот. создается
                       коммент.
    """
    refer_to_pk = data.get("refer_to")
    if refer_to_pk:
        refer_to = Comment.objects.filter(pk=refer_to_pk)
        if not refer_to.exists():
            raise Http404()
    else:
        refer_to = None
    model_class = TYPE_MATCH_MAP[data["article_type"]]
    object = get_object_or_404(model_class, ok=data["object_id"])
    c = Comment.objects.create(refer_to=refer_to,
                               object=object,
                               text=data["text"],
                               user=data["user"],
                               )
    return c


def update_comment(comment_pk, user, text):
    """Обновление комментария.
       Args:
            comment_pk: PK комментария для обновления. Число.
            user: Владелец комментария для обновления.
            text: Новый текст комментария. Текст.
       Returns:
               comments.Comment - обновленный комментарий
       Raises:
                Http404 - если комментарий не найден.
    """
    try:
        c = (Comment.objects
             .select_for_update()
             .get(pk=comment_pk, user=user))
    except Comment.DoesNotExist:
        raise Http404()
    else:
        c.update(text=text)
        return c
        #TODO: notify


def delete_comment(comment_pk, user):
    """Удаление комментария.
        Args:
             comment_pk: PK комментария для удаления. Число.
             user: Владелец комментария для удаления.
        Raises:
               Http404 - если комментарий не найден.
    """
    try:
        (Comment.objects
         .select_for_update()
         .filter(pk=comment_pk, user=user)
         .update(deleted=True))
    except Comment.DoesNotExist:
        raise Http404()
        #TODO: notify