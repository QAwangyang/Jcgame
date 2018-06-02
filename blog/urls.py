from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^blog/index',views.index),
    url(r'^blog/dongche',views.dongche),
    url(r'^blog/honghuanglan',views.ryb),
    url(r'^blog/python_jira',views.python_jira),
    url(r'^blog/cocos_performance',views.cocos_performance),
]