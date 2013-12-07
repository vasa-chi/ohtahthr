# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Base(models.Model):
    """Базовая модель для все моделей в системе."""
    title = models.CharField(u"название", max_length=255)
    url = models.URLField(u"ссылка", null=True, blank=True)
    rating = models.IntegerField(verbose_name=u"рейтинг", default=0)
    added_by = models.ForeignKey(User, verbose_name=u"добавил")
    date = models.DateTimeField(auto_now_add=True, verbose_name=u"дата добавления")
    last_edit = models.DateTimeField(auto_now_add=True, auto_now=True, verbose_name=u"дата последнего изменения")
    description = models.TextField(null=True, blank=True)
    company = models.CharField(u"Компания, к которой относится %(class)s", max_length=255)
    tags = TaggableManager(verbose_name=u"теги", blank=True)
    deleted = models.BooleanField(verbose_name=u"удалено?", default=False)

    class Meta:
        abstract = True


class Company(models.Model):
    """Модель для комании."""
    title = models.CharField(u"название", max_length=255, unique=True)

    def __unicode__(self):
        return self.title