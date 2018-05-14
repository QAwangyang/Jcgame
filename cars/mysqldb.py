# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from cars.models import users_car
 
# 数据库操作
def testdb(request):
    test1 = users_car(ip='0.0.0.1',isvisite='1',carcount="5",mulitple="5",visitetime="1521828763")
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")