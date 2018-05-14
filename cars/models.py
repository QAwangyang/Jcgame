# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class users_car(models.Model):
    ip = models.CharField(max_length=50)
    isvisite = models.IntegerField()
    carcount = models.IntegerField()
    mulitple = models.IntegerField()
    visitetime = models.CharField(max_length=50)