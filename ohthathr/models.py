# -*- coding: utf-8 -*-
from comments.models import Comment
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.generic import GenericRelation
from taggit.managers import TaggableManager


class Base(models.Model):
    """Базовая модель для все моделей в системе."""
    title = models.CharField(u"название", max_length=255)
    url = models.URLField(u"ссылка", null=True, blank=True)
    rating = models.IntegerField(verbose_name=u"рейтинг", default=0)
    added_by = models.ForeignKey(User, verbose_name=u"добавил")
    date = models.DateTimeField(auto_now_add=True, verbose_name=u"дата добавления")
    last_edit = models.DateTimeField(auto_now=True, verbose_name=u"дата последнего изменения", null=True, default=None)
    description = models.TextField(verbose_name=u"Описание")
    tags = TaggableManager(verbose_name=u"теги", blank=True)
    deleted = models.BooleanField(verbose_name=u"удалено?", default=False)
    comments = GenericRelation(Comment)

    class Meta:
        abstract = True
        ordering = ["-date"]

    def __unicode__(self):
        return self.title