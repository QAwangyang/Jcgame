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

def select_order_by(sql_name,by_name,cursor):
	cursor.execute('select * from ' + sql_name +' order by '+ by_name + " desc")
	res=cursor.fetchall()
	return res

def index(request):
	cursor=connection.cursor()
	liked_news = select_all("rightbox",cursor)
	print liked_news
	newslist = select_order_by("blog_news","time",cursor)
	print newslist
	# cursor.execute("UPDATE follow SET followid = 10 WHERE userid = '8' ")    
	#transaction.commit_unless_managed()

	# for i in res:
	# 	print i.id
	cursor.close()
	return render(request,'blog/blog.html',{"newslist":newslist,"liked_news":liked_news})

def dongche(request):
	cursor=connection.cursor()
	newslist = select_all("blog_news",cursor)
	cursor.close()
	return render(request,'blog/dongche.html',{"newslist":newslist})


def ryb(request):
	return render(request,'blog/RYB.html')

def python_jira(request):
	return render(request,'blog/python_jira.html')