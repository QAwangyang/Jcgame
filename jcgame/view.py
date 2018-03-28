from django.http import HttpResponse
from django.shortcuts import render
import tools
import sys  
import json

reload(sys)
sys.setdefaultencoding('utf8')
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def mainpage(request):
    return render(request, 'jcgame.html')
