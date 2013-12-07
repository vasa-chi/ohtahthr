# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model


class Comment(models):
    refer_to = models.ForeignKey("self", verbose_name=u"родительский комментарий", null=True, blank=True)
    text = models.TextField(max_length=2000, verbose_name=u"комментарий")
    object = GenericForeignKey()
    object_id = models.ForeignKey(verbose_name=u"id объекта комментария", null=True, blank=True)
    content_type = models.ForeignKey(ContentType, null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name=u"дата создания")
    date_edited = models.DateTimeField(auto_now=True, auto_now_add=True)
    deleted = models.BooleanField(verbose_name=u"удален", default=False)
    user = models.ForeignKey(get_user_model(), verbose_name=u"пользователь", null=True, blank=True)

    class Meta:
        verbose_name = u"комментарий"