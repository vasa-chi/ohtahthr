# -*- coding: utf-8 -*-
from taggit.models import Tag
from interviews.models import Interview
from vacancies.models import Vacancy
from comments.models import Comment

TYPE_MATCH_MAP = {
    0: Vacancy,
    1: Interview,
    2: Comment
}