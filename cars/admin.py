# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import users_car


@admin.register(users_car)
class BlogAdmin(admin.ModelAdmin):
    list_display=('ip', 'isvisit', 'car_counts', 'multiple','visittime')


# Register your models here.
