from django.test import TestCase
from .models import location

# Create your tests here.

class locationTestClass(TestCase):
    # set up method

   lass locationTestClass(TestCase):
   """
   Tests location class and its functions
   """
   #Set up method
   def setUp(self):
       self.loc = Location()

   def test_instance(self):
       self.assertTrue(isinstance(self.loc, Location))
    
