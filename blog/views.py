# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.db import connection




# Create your views here.

# def blog(request):
# 	# res=cursor.execute('select * from hello_author')
# 	# print (res)
# 	return render(request, 'blog.html')


def select_all(sql_name,cursor):
	cursor.execute('select * from ' + sql_name)
	res=cursor.fetchall()
	return res

def index(request):
	cursor=connection.cursor()
	liked_news = select_all("rightbox",cursor)
	print liked_news
	newslist = select_all("news",cursor)
	# cursor.execute("UPDATE follow SET followid = 10 WHERE userid = '8' ")    
	#transaction.commit_unless_managed()

	# for i in res:
	# 	print i.id
	cursor.close()
	return render(request,'blog/blog.html',{"newslist":newslist,"liked_news":liked_news})

def dongche(request):
	cursor=connection.cursor()
	newslist = select_all("news",cursor)
	cursor.close()
	return render(request,'blog/dongche.html',{"newslist":newslist})