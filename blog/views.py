# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.db import connection

cursor=connection.cursor()


# Create your views here.

# def blog(request):
# 	# res=cursor.execute('select * from hello_author')
# 	# print (res)
# 	return render(request, 'blog.html')


def select_all(sql_name):
	cursor.execute('select * from ' + sql_name )
	res=cursor.fetchall()
	return res

def index(request):
	
	liked_news = select_all("rightbox")
	newslist = select_all("news")
	# cursor.execute("UPDATE follow SET followid = 10 WHERE userid = '8' ")    
	#transaction.commit_unless_managed()

	# for i in res:
	# 	print i.id
	return render(request,'blog.html',{"newslist":newslist,"liked_news":liked_news})