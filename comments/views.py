# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from api import create_comment, update_comment, delete_comment
from json import loads


class CommentCreateView(View):

    def post(self, request, *args, **kwargs):
        from django.contrib.auth.models import User
        user = User.objects.get(pk=1)  # TODO: remove placeholder
        comment_data = loads(request.POST["comment_data"])
        comment_data["user"] = user
        comment = create_comment(comment_data)
        return render(request, "comments/comment.html", {"comment": comment})


class CommentDeleteView(View):

    def post(self, request, *args, **kwargs):
        from django.contrib.auth.models import User
        user = User.objects.get(pk=1)  # TODO: remove placeholder
        comment_data = loads(request.POST["comment_data"])
        delete_comment(comment_data["pk"], user)
        return HttpResponse()


class CommentUpdateView(View):

    def post(self, request, *args, **kwargs):
        from django.contrib.auth.models import User
        user = User.objects.get(pk=1)  # TODO: remove placeholder
        comment_data = loads(request.POST["comment_data"])
        comment = update_comment(comment_data["pk"], comment_data["text"], user)
        return render(request, "comments/comment.html", comment=comment)