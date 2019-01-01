from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^blog/index',views.index),
    url(r'^blog/dongche',views.dongche),
    url(r'^blog/honghuanglan',views.ryb),
    url(r'^blog/python_jira',views.python_jira),
    url(r'^blog/cocos_performance',views.cocos_performance),
    url(r'^blog/locust',views.locust),
    url(r'^blog/atx_server',views.atx_server),
    url(r'^blog/get_more_news',views.get_more_news),
    url(r'^blog/like',views.like),
]