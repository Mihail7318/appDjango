from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.template.defaulttags import register

from news.models import Post
from .models import *



#slider
def slider(request):
    slider = Slider.objects.all()
    context = {
        'slider': slider,
        'title': 'Главная'
    }
    return render(request, 'glavnaya/glavnaya.html', context=context )



class Home(ListView) :
    model = Favorites
    template_name = 'glavnaya/glavnaya.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context