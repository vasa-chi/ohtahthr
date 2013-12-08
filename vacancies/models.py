# -*- coding: utf-8 -*-
from ohthathr.models import Base
from django.db import models


class Vacancy(Base):
    """Модель представления вакансии.
       Здесь будут лежать вакансии из wat-парада, а так же вакансии с
       собеседований и самые интересные вакансии. Основная модель
       проекта, вроде как.

       Attributes:
        type: Тип вакансии. Целое число, VACANCY_TYPE_CHOICES.
        title (derived): название. Строка.
        url (derived): ссылка на вакансию. Ссылка на внешний ресурс,
                       Необходимо помнить, что мы должны либо выгружать
                       и парсить то, что идет по ссылке (либо хранить
                       скриншоты?). Строка url.
        rating (derived): Рейтинг. Целое число.
        added_by (derived): Кто добавил. Fk на пользователя.
        date (derived): Дата добавления. DateTime.
        last_edit (derived): Дата последнего редактирования. DateTime.
        description (derived): Описание вакансии и прочее. Строка.
        company (derived): Название компании, чью вакансия.
        why: В зависимости от типа вакансии может предоставлять :
             1 - Почему эта вакансия попала в wat-парад
             2 - null
             3 - Почему эта вакансия интересна

    """
    VACANCY_TYPE_CHOICES = ((1, u"Вакансия из парада"),
                            (2, u"Вакансия из историй"),
                            (3, u"Вакансия мечты")
                            )
    type = models.PositiveSmallIntegerField(verbose_name=u"тип вакансии", choices=VACANCY_TYPE_CHOICES)
    why = models.TextField(verbose_name=u"Почему добавлена", null=True, blank=True)