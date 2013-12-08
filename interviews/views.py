# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from models import Interview
from forms import InterviewForm
from api import create_interview, delete_interview, update_interview


class InterviewListView(ListView):
    queryset = (Interview.objects.filter(deleted=False)
                         .select_related("added_by")
                         .prefetch_related('tagged_items__tag'))
    template_name = "interview_list.html"

    def get_queryset(self):
        qs = super(InterviewListView, self).get_queryset()#.filter(added_by=self.request.user)
        return qs

    #def get(self, request, *args, **kwargs):
    #    TODO: ordering, filter by settings
    #    pass


class InterviewDetailView(DetailView):
    queryset = (Interview.objects.filter(deleted=False)
                         .select_related("added_by", "comments", "comments__user")
                         .prefetch_related('tagged_items__tag'))
    template_name = "interview_detail.html"

    def get_queryset(self):
        qs = super(InterviewDetailView, self).get_queryset()#.filter(added_by=self.request.user)
        return qs


class InterviewCreateView(CreateView):
    template_name = "interview_create.html"
    queryset = (Interview.objects.filter(deleted=False)
                         .prefetch_related('tagged_items__tag'))
    form_class = InterviewForm

    def get_success_url(self):
        return reverse("fuji_detail", kwargs={"pk": self.object.pk})

    def get_queryset(self):
        return super(InterviewCreateView, self).get_queryset()#.filter(added_by=self.request.user)

    def post(self, request, *args, **kwargs):
        from django.contrib.auth.models import User
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            form.cleaned_data["added_by"] = User.objects.get(pk=1)  # self.request.user
            self.object = create_interview(form.cleaned_data)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)