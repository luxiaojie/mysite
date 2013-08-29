from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response 
import datetime

def hello(request):
	return HttpResponse("Hello world!")

def xxx(request):
	return HttpResponse("Hello world!")

def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html',{'current_date':now})



def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html ="<html><body>In %s hour(s), it will be %s.</body></html>" %(offset,dt)
	return HttpResponse(html)

def search(request):
	if 'q' in request.GET:
		message = 'You searched for: %r' % request.GET['q']
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)
