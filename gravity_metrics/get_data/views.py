from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from gravity_metrics.get_data import models
from gravity_metrics.get_data.models import *

def get_data(request):
	if request.method == 'GET':
		device_n = request.GET['i']
		device = Device(device = device_n)
		device.save()
		timestamp = request.GET['t']
		delta = request.GET['d']
		a = Delta(device = device, timestamp = timestamp, delta = delta)
		a.save()
		return HttpResponse(200)
	return HttpResponse(200)

def order_by_time(request):
	delta_by_timestamp = Delta.objects.order_by('timestamp') # order_by doesn't work yet; needs QuerySet API
	context = {'delta_by_timestamp': delta_by_timestamp}
	return render(request, 'get_data/order_by_time.html', context)

def order_by_device(request):
	delta_by_device = Delta.objects.order_by('device') # order_by doesn't work yet. See above
	context = {'delta_by_device': delta_by_device}
	return render(request, 'get_data/order_by_device.html', context)

