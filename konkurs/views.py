from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Fed, Reg

#Fed
def fed(request):
    fed = Fed.objects.all()
    context = {
        'feds': fed,
    }
    return render(request, 'konkurs/Fed.html', context=context )

#Reg
def reg(request):
    reg = Reg.objects.all()
    context = {
        'reg': reg,
    }
    return render(request, 'konkurs/Reg.html', context=context )
