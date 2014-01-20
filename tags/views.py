# -*- coding: utf-8 -*-
from django.views.generic import View
from django.http import HttpResponse
from tags.models import CountedTag
from api import search_by_tag
from json import dumps


class TagFeed(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(dumps(list(CountedTag.objects.filter(name__icontains=request.GET["q"])
                                                  .values_list("name", flat=True))),
                            content_type="application/json")


class SearchByTag(View):

    def get(self, request, *args, **kwargs):
        tagname = request.GET.get("q")
        content = search_by_tag(tagname) if tagname else []
        return HttpResponse(content=dumps(content), content_type="application/json")