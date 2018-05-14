# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import django.utils.timezone as timezone

import os


class news(models.Model):
    tittle = models.CharField(u'标题',max_length=250)
    contact = models.TextField()
    picture = models.ImageField(u'图片')
    time = models.DateTimeField(u'发表时间', default = timezone.now)
