# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from pirate_site.models import *
from django.db.models import get_app, get_models
from operator import attrgetter
from itertools import chain


def index(request):
    context = ''
    return render(request, 'home/home.html', context)


def browse(request):
    files_list = []
    for model in get_models(get_app('pirate_site')):
        files_list = chain(files_list, (model.objects.order_by('-date_uploaded').all()))
    files_list = sorted(files_list, key=attrgetter('date_uploaded'), reverse=True)
    context = {'data': files_list}
    return render(request, 'pirate_site/browse.html', context)


def help(request):
    return render(request, 'pirate_site/help.html')


def category(request, category):
    for model in get_models(get_app('pirate_site')):
        if category == model.__name__.lower():
            files_list = model.objects.order_by('-date_uploaded').all()
#            output = '<br>'.join([e.title for e in files_list])
            context = {'data': files_list, 'category': category}
            return render(request, 'pirate_site/category.html', context)
            break
    raise Http404


def detail(request, category, id):
    for model in get_models(get_app('pirate_site')):
        if category == model.__name__.lower():
            output = get_object_or_404(model, id=id)
            context = {'data': output}
            return render(request, 'pirate_site/detail.html', context)
            break
    return HttpResponse("No such category found.")
