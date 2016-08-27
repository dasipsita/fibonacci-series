from django.test import TestCase
import views

class SimpleTest(TestCase):
    def test_basic_fibonacci_number(self):
        """
        Tests cases for finding the nth fibonacci number
        """
        self.assertEqual(0 , views.fibonacci(0))
        self.assertEqual(1 , views.fibonacci(1))
        self.assertEqual("Negative argument. Invalid input_range." , views.fibonacci(-8))
        self.assertEqual(832040 , views.fibonacci(30))
  


