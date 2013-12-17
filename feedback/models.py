# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class UserFeedback(models.Model):
    TYPE_CHOICES = ((0, u"Ошибка в работе сайта"),
                    (1, u"Уязвимость на сайте"),
                    (2, u"Нарушение правил сайта"),
                    (3, u"Блокировка аккаунта"),
                    (4, u"Предложение сотрудничества"),
                    (5, u"Другое"),)

    text = models.TextField(verbose_name=u"сообщение")
    email = models.EmailField(verbose_name=u"email")
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)
    type = models.PositiveSmallIntegerField(verbose_name=u"Тема", choices=TYPE_CHOICES, default=2)
    object = GenericForeignKey("content_type", "object_id")
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_type = models.ForeignKey(ContentType, null=True, blank=True)