# Create your views here.

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from pirate_site.models import *
from django.db.models import get_app, get_models


def index(request):
    return HttpResponse("Search box + Welcome Page")


def category(request, category):
    for model in get_models(get_app('pirate_site')):
        if category == model.__name__.lower():
            files_list = model.objects.order_by('title').all()
            output = '<br>'.join([e.title for e in files_list])
            return HttpResponse(output)
            break
    return HttpResponse("No such category found.")


def detail(request, category, id):
    for model in get_models(get_app('pirate_site')):
        if category == model.__name__.lower():
            # files_list = model.objects.filter(id=id)
            output = get_object_or_404(model, id=id)
            return HttpResponse(output)
            break
    return HttpResponse("No such category found.")
