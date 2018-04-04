# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import tools
import sys  
import json
from django.db import connection
import time



def is_connection_usable():
	try:
		cursor.connection.ping()
		return True
	except:
		cursor=connection.close()
		return False


def cars(request):

	return render(request, 'cars.html')


def user_status(x,ip,t,cd,sql_update,cursor):
	
	if(t==None):
		t=0
	if(x-int(t)>cd):
		cursor.execute(sql_update)
		return 1
	else:
		return 0

def car_counts(request):

	#print (is_connection_usable())

	cursor=connection.cursor()

	if request.POST:
		multiple = request.POST['multiple']	#倍数
		if int(multiple) >10:
			return HttpResponse(0, content_type="application/json")
		car_counts = tools.get_car_counts(int(multiple))   #查询了多少次
		year_res = tools.get_car_year(car_counts) #年月
		x=int(time.time()) #当前时间
		ip = tools.get_user_ip(request) #ip

		sql_seach = "select * from users_car where ip= '%s' " %str(ip)
		sql_insert = "insert into users_car(ip,isvisit,car_counts,multiple,visittime) VALUES( '%s',1,'%d','%s','%s')" %(str(ip),car_counts,multiple,x)
		sql_update = "update users_car set visittime = '%d',car_counts='%d',multiple='%s' where ip= '%s' " %(x,int(car_counts),multiple,str(ip))
		#print sql_insert
		cursor.execute(sql_seach)
		res=cursor.fetchall()


		if (len(res)==0):  #if sql has
			cursor.execute(sql_insert)
			re_str="恭喜你<br/>"

		elif(user_status(x,ip,res[0][5],3600,sql_update,cursor)):  #if cold down
			re_str="恭喜你<br/>"	

		else:
			if(int(multiple) == res[0][4]):
				re_str="结果不会变的，攒攒人品过会儿再来<br/>"
			else:
				re_str="你换成"+str(multiple)+"倍,结果也不会变的<br/>"
				cursor.execute("update users_car set multiple='%s' where ip= '%s' " %(multiple,str(ip)))

			car_counts = res[0][3]
			year_res = tools.get_car_year(car_counts)			

		re={
			"year":year_res["year"],
			"month":year_res["month"],
			"str":re_str,
			"multiple":multiple
			}
		cursor.close()

	return  HttpResponse(json.dumps(re), content_type="application/json")


# Create your views here.
