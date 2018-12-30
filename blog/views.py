# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import json



# Create your views here.

# def blog(request):
# 	# res=cursor.execute('select * from hello_author')
# 	# print (res)
# 	return render(request, 'blog.html')


def select_all(sql_name,cursor):
	cursor.execute('select * from ' + sql_name)
	res=cursor.fetchall()
	return res

def select_order_by(sql_name,by_name,cursor,init,count):
	cursor.execute('select * from ' + sql_name +' order by '+ by_name + " desc limit "+ init+","+count)
	res=cursor.fetchall()
	return res

def index(request):
	cursor=connection.cursor()
	liked_news = select_all("rightbox",cursor)
	print liked_news
	newslist = select_order_by("blog_news","time",cursor,"0","5")
	print newslist
	# cursor.execute("UPDATE follow SET followid = 10 WHERE userid = '8' ")    
	#transaction.commit_unless_managed()

	cursor.close()
	return render(request,'blog/blog.html',{"newslist":newslist,"liked_news":liked_news})

def get_more_news(request):
	cursor=connection.cursor()
	resp=[]
	#print "fuck"
	if request.POST:
		#print "fuck"
		page_num = request.POST['page_num']	#倍数
		init_num=int(page_num)*5
		#print "***************",page_num
		newslist = select_order_by("blog_news","time",cursor,str(init_num),"5")
		#print newslist
		cursor.close()
		for response in newslist:
			re={}
			re["title"]=response[1]
			re["body"]=response[2]
			re["pic_name"]=response[3]
			re["date"]=str(response[4])
			resp.append(re)
		#print resp
		return HttpResponse(json.dumps(resp), content_type="application/json")

def dongche(request):
	cursor=connection.cursor()
	newslist = select_all("blog_news",cursor)
	cursor.close()
	return render(request,'blog/dongche.html',{"newslist":newslist})


def ryb(request):
	return render(request,'blog/RYB.html')

def python_jira(request):
	return render(request,'blog/python_jira.html')

def cocos_performance(request):
	return render(request,'blog/cocos_performance.html')

def atx_server(request):
	return render(request,'blog/atx_server.html')

def locust(request):
	return render(request,'blog/locust.html')