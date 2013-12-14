# -*- coding: utf-8 -*-
from django.views.generic import View
from django.http import HttpResponse
from api import rating_manipulation
from json import dumps, loads


class RatingView(View):

    def post(self, request, *args, **kwargs):
        data = loads(request.POST["rating_data"])
        from django.contrib.auth.models import User
        data["user"] = User.objects.get(pk=1)  # request.user TODO: remove placeholder
        return HttpResponse(dumps({"rating":rating_manipulation(data)}, content_type="application/json"))