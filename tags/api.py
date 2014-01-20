# -*- coding: utf-8 -*-
from ohthathr.api import search


def search_by_tag(tag_name):
    """Производит поиск записей по названию тега.

       Args:
            tag_name: Название тега. Строка.
       Returns:
            Результат работы функции ohthathr.api.search
            с параметром by_tag=True.

       """
    return search(tag_name, only_by_tag=True)