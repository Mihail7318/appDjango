from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import F


class Home(ListView) :
    model = Smena
    template_name = 'profsmen/profsmena.html'
    context_object_name = 'smenas'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.LANGUAGE_CODE == "ru":
            context['title'] ="Рубрики "
        if self.request.LANGUAGE_CODE == "en":
            context['title'] ="Categories"


        return context

class GetPost(DetailView):
    model = Smena
    template_name = 'profsmen/profsmenadetails.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        # self.object.refresh_from_db()
        return context