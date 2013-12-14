# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class Comment(models.Model):
    """Модель комментария.

       Attributes:
                  refer_to: Ссылка на родительский комментарий. На себя же.
                  text: Текст комментария.
                  object: Дженерик FK для
                  object_id: Значение id для ссылки на дженерик объект.
                  content_type: FK на контент тайп для ссылки на объект.
                  date: Датавремя создания.
                  date_edited: Датавремя редактирования
                  deleted: Удален? Boolean, не отображаем удаленных в списках.
                  user: Ссылка на пользователя, создавшего комментарий.
                  rating: Рейтинг комментария.
    """
    refer_to = models.ForeignKey("self", verbose_name=u"родительский комментарий", null=True, blank=True,
                                 related_name="childs")
    text = models.TextField(max_length=2000, verbose_name=u"комментарий", null=False, blank=False)
    object = GenericForeignKey("content_type", "object_id")
    object_id = models.PositiveIntegerField(verbose_name=u"id объекта комментария", null=True, blank=True)
    content_type = models.ForeignKey(ContentType, null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name=u"дата создания")
    date_edited = models.DateTimeField(auto_now=True, default=None, null=True, blank=True)
    deleted = models.BooleanField(verbose_name=u"удален", default=False)
    user = models.ForeignKey(User, verbose_name=u"пользователь", null=True, blank=True)
    rating = models.IntegerField(verbose_name=u"рейтинг", default=0)

    class Meta:
        verbose_name = u"комментарий"
        ordering = ["-date"]

    def get_item_type(self):
        return 2