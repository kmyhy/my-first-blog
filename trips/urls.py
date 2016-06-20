from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^hello/$',views.hello_world),
	url(r'^$',views.home),
	url(r'^trip/(?P<pk>\d+)/$', views.trip_detail,name='trip_detail'),
]