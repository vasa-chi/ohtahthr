# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class RatedByUser(models.Model):
    """Модель для хранящая информацию о воздействии пользователя на рейтинг.

    object: Дженерик FK для
    object_id: Значение id для ссылки на дженерик объект.
    content_type: FK на контент тайп для ссылки на объект.
    user: Ссылка на пользователя, осуществившего манипуляцию с рейтингом.
    action_type: Тип действия с рейингом. 0 - '-'. 1 - '+';

    """

    ACTION_TYPE_CHOICES = ((0, "0"),
                           (1, "+"))

    object = GenericForeignKey("content_type", "object_id")
    object_id = models.PositiveIntegerField(verbose_name=u"id объекта комментария", null=True, blank=True)
    content_type = models.ForeignKey(ContentType, null=True)
    user = models.ForeignKey(User, verbose_name=u"пользователь")
    action_type = models.PositiveSmallIntegerField(verbose_name=u"тип действия", choices=ACTION_TYPE_CHOICES)

    class Meta:
        verbose_name = u"запись о изменении рейтинга пользователем"