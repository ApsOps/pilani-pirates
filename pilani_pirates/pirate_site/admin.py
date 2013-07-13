from django.contrib import admin
from pirate_site.models import *
from django.db.models import get_app, get_models

for model in get_models(get_app('pirate_site')):
    admin.site.register(model)
