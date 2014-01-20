# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from api import search
from json import dumps
from exceptions import NotImplementedError


class BaseListView(ListView):
    allow_empty = True
    paginate_by = 10

    def get_queryset(self):
        return (super(BaseListView, self).get_queryset()
                                         .filter(deleted=False)  # filter(deleted=False, added_by=self.request.user)
                                         .select_related("added_by")
                                         .prefetch_related('tagged_items__tag'))

    #def get(self, request, *args, **kwargs):
    #    TODO: ordering, filter by settings
    #    pass


class BaseDetailView(DetailView):

    def get_queryset(self):
        return (super(BaseDetailView, self).get_queryset()
                                           .filter(deleted=False)  #TODO: filter(deleted=False, added_by=self.request.user)
                                           .select_related("added_by", "comments", "comments__user")
                                           .prefetch_related('tagged_items__tag'))


class BaseCRUDMixin(object):
    success_url = None

    def get_queryset(self):
        return (super(BaseCRUDMixin, self).get_queryset()
                                          .filter(deleted=False)  #TODO: filter(deleted=False, added_by=self.request.user)
                                          .select_related("added_by", "comments", "comments__user")
                                          .prefetch_related('tagged_items__tag'))

    def get_object(self, queryset=None):
        qs = self.get_queryset()
        try:
            return qs.get(pk=self.kwargs["pk"])  # , TODO added_by=self.request.user)
        except self.model.DoesNotExist:
            raise Http404()

    def get_success_url(self):
        return reverse(self.success_url, kwargs={"pk": self.object.pk})

    def prepare_api_data(self, form_cleaned_data):
        return form_cleaned_data

    @property
    def api_function(self):
        return self._get_api_function()

    def _get_api_function(self):
        raise NotImplementedError


class BaseCreateView(BaseCRUDMixin, CreateView):

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            api_data = self.prepare_api_data(form.cleaned_data)
            self.object = self.api_function(api_data)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class BaseUpdateView(BaseCRUDMixin, UpdateView):

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            if form.has_changed():
                api_data = self.prepare_api_data(form.cleaned_data)
                self.api_function(self.object, api_data)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class BaseDeleteView(BaseCRUDMixin, DeleteView):

    def get_success_url(self):
        return reverse(self.success_url)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.api_function(self.object)
        return HttpResponseRedirect(self.get_success_url())


class SearchView(View):

    def get(self, request, *args, **kwargs):
        term = request.GET.get("q")
        content = search(term) if term else []
        return HttpResponse(content=dumps(content), content_type="application/json")