# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class users_car(models.Model):
    ip = models.CharField(max_length=50)
    isvisit = models.IntegerField()
    car_counts = models.IntegerField()
    multiple = models.IntegerField()
    visittime = models.CharField(max_length=50)