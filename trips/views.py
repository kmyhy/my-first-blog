from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Trip

def hello_world(request):
	return render(request, 'hello_world.html', {
        'current_time': datetime.now(),
    })

def home(request):
	trip_list=Trip.objects.all()
	return render(request,'home.html',{'trip_list':trip_list})

def trip_detail(request,pk):
	trip=Trip.objects.get(pk=pk)
	return render(request,'trip_detail.html',{'trip':trip})