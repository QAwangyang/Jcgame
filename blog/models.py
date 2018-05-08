# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class news(models.Model):
    tittle = models.CharField(u'标题',max_length=250)
    contact = models.TextField()
    picture = models.ImageField(u'图片',upload_to='upload/')
    time = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)