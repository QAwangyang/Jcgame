# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import news 

# Register your models here.
@admin.register(news)
class BlogAdmin(admin.ModelAdmin):
    list_display=('tittle', 'contact', 'picture', 'time')