#-*- encoding:utf-8 -*-
import random
import datetime

# def get_user_ip(request):

# 	if request.META.has_key('HTTP_X_FORWARDED_FOR'):
# 		ip =  request.META['HTTP_X_FORWARDED_FOR']
# 	else:
# 		ip = request.META['REMOTE_ADDR']

# 	return ip

def get_user_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[-1].strip()
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip
	
def get_car_counts(Multiple=1):  #算倍数
	n=1
	index_list=[]
	counts=1

	print "jinlai le "

	while n<=Multiple:
		index=random.randint(0,900)
		index_list.append(index)
		n+=1
		pass

	print index_list

	while 1:
		target_num = random.randint(0,900)
		for x in index_list:
			if (x==target_num):
				return counts
			else:
				pass
		counts+=1

def get_car_year(counts):
	res={}
	now_year = datetime.datetime.now().year
	now_month = datetime.datetime.now().month

	if (int(now_month)%2 != 0):
		now_month+=1
	else:
		pass

	year = int (counts/6)+int(now_year)
	month = int (counts%6)*2+ int(now_month)
	if (month > 12):
		month -=12
		year +=1
	res['year']=year
	res['month']=month
	return res

