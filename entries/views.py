import json
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404, HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic.edit import CreateView

from models import Entry
from forms import EntryForm


class DetailView(TemplateView):
    template_name = 'detail.html'

class CreateEntryView(CreateView):
    model = Entry
    template_name = 'index.html'
    form_class = EntryForm
    success_url = '.'

    def get_form(self, form_class):
        form = super(CreateEntryView, self).get_form(form_class)
        # Return user online
        try:
            form.instance.user = self.request.user
        except:
            pass
        return form

    def form_valid(self, form):
        from django.contrib import messages
        messages.success(self.request, "Entrada creada.")

        return super(CreateEntryView,self).form_valid(form)
