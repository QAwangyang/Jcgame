from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^blog/index',views.index),
    url(r'^blog/dongche',views.dongche),
]