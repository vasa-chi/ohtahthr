# -*- coding: utf-8 -*-
from django.views.generic import View
from django.http import HttpResponse
from taggit.models import Tag
from json import dumps


class TagFeed(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(dumps(list(Tag.objects.filter(name__icontains=request.GET["q"])
                                                  .values_list("name",flat=True))),
                            content_type="application/json")