from django.shortcuts import render, render_to_response, HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
import time
import json


@csrf_protect
def home(request):
	context = RequestContext(request)
	start_time = time.time()
	print start_time
	input_range = ''
	if request.method == 'POST':
		input_range = request.POST['range']
		print type(input_range)
		print str(input_range)	
	if input_range:
		response = get_result(int(input_range))
		end_time=time.time()
		print end_time
		taken_time = float(end_time) - float(start_time)
		print taken_time
		return HttpResponse(json.dumps({'response': response, 'taken_time':taken_time}))
	else:			
		return render_to_response('home.html', context)

def get_result(input_range):
	a,b = 1,1
	for i in range(1,input_range):
		a,b = b,a+b
		print a
	return a	




