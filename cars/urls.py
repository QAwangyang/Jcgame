from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^cars$',views.cars),
    url(r'^cars/car_counts$',views.car_counts),
]