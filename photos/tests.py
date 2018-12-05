from django.test import TestCase
from .models import location

# Create your tests here.

class locationTestClass(TestCase):
    # set up method

    def setUp(self):
        self.location=location(location)

    
