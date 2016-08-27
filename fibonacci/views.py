from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
import time
import json
from gmpy2 import mpfr

@csrf_protect
def home(request):
	"""
	:param Input range
	:purpose Inputs a range and calls the function to calculate the fibonacci number
	:return The nth fibonacci number and total time taken to calculate the fibonacci number
	"""
	context = RequestContext(request)
	input_range = ''
	if request.method == 'POST':
		input_range = request.POST['range']
		print type(input_range)
		print "given range: ",input_range
		start_time = time.time()
		print "starting time: ",start_time
		fib = fibonacci(int(input_range))
		response = mpfr(fib)
		end_time=time.time()
		print "result: ",response
		total_time = float(end_time) - float(start_time)
		time_taken = "{0:.6f}".format(total_time)
		print "total taken time: ",time_taken
		return HttpResponse(json.dumps({'response': str(response), 'total_time':time_taken}))
	else:			
		return render_to_response('home.html', context)

def fibonacci(n):
	"""
	:param Input range
	:purpose Inputs a range and calls the actual function to calculate the fibonacci number
	:return The nth fibonacci number
	"""
	if n < 0:
		return "Negative argument. Invalid input_range."
	return fib(n)[0]

def fib(n):
	"""
	:param Input range
	:purpose Inputs a range and calculates nth and (n+1)th fibonacci numbers
	:return A tuple containing (F(n), F(n+1))
	"""
	if n == 0:
		return (0, 1)
	else:
		a, b = fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)



