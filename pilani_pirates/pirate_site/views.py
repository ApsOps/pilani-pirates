# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from pirate_site.models import *


def index(request):
    context = ''
    return render(request, 'home/home.html', context)


def browse(request):
    files_list = File.objects.order_by('-date_uploaded').all()
    context = {'data': files_list}
    return render(request, 'pirate_site/browse.html', context)


def help(request):
    return render(request, 'pirate_site/help.html')


def category(request, category):
        files_list = File.objects.order_by('-date_uploaded').filter(category=category)
        context = {'data': files_list, 'category': category}
        return render(request, 'pirate_site/category.html', context)


def detail(request, category, id):
    output = get_object_or_404(File, id=id, category=category)
    context = {'data': output, 'category': category}
    return render(request, 'pirate_site/detail.html', context)
