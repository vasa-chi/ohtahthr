# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from ohthathr.models import Base


class Interview(Base):
    """ Модель отображающая собеседование.
        Имеется ввиду - историю о себеседовании
    Attributes:
         title (derived): название. Строка.
         url (derived): ссылка на вакансию. Ссылка может вести как на наш
                        ресурс, так и на внешний. Необходимо помнить, что
                        мы должны либо выгружать и парсить то, что идет по
                        ссылке (либо хранить скриншоты?). Строка url.
        rating (derived): Рейтинг. Целое число.
        added_by (derived): Кто добавил. Fk на пользователя.
        date (derived): Дата добавления. DateTime.
        last_edit (derived): Дата последнего редактирования. DateTime.
        description (derived): История и описание интервью. Строка.
        company (derived): Название компании, где было интервью.

    """
    WAS_SUCCESS_CHOICES = ((1, u"Да"),
                           (2, u"Нет"))

    was_success = models.SmallIntegerField(verbose_name=u"успешно?", choices=WAS_SUCCESS_CHOICES,
                                           default=None, null=True, blank=True)

    class Meta:
        verbose_name = u"собеседование"

    def get_absolute_url(self):
        return reverse("interview_detail", kwargs={"pk": self.pk})

    def get_new_heading(self):
        return u"Новая история собеседования"

    def get_edit_heading(self):
        return u"{0} - редактирование".format(self.title)

    def get_item_type(self):
        return 1