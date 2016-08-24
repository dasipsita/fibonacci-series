from django.test import TestCase
import views
# Create your tests here.

class SimpleTest:
	def __init__(self,n):
		"""
		Tests that for range 5 fibonacci number is 5.
		"""
		response = views.get_result(n)
		if response == 5:
			print "function working correctly"
		else:	
			print "function is not working correctly"

SimpleTest(5)

	   


