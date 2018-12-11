from django.test import TestCase
from .models import location

# Create your tests here.

class locationTestClass(TestCase):
    """
    Tests Location class and its functions
    """
    #Set up method
    def setUp(self):
        self.locale = Location(name='here', description='testing pic')

    def test_instance(self):
        self.assertTrue(isinstance(self.locale, Location))

    def test_save_method(self):
        """
        Function to test that location is being saved
        """
        self.locale.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        """
        Function to test that a location can be deleted
        """
        self.locale.save_location()
        self.locale.delete_location()
        self.assertTrue(len(locations) == 0)
    
    def test_update_method(self):
        """
        Function to test that a location's details can be updates
        """
        self.locale.save_location()
        new_place = Location.objects.filter(name='here').update(name='hapa')
        locations = Location.objects.get(name='hapa')
        self.assertTrue(locations.name, 'hapa')


class CategoryTestClass(TestCase):
    """
    Tests category class and its functions
    """
    #Set up method
    def setUp(self):
        self.cat = Category(name='this', description='testing pic')
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))
    
    def test_save_method(self):
        """
        Function to test that category is being saved
        """
        self.cat.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_method(self):
        """
        Function to test that a category can be deleted
        """
        self.cat.save_category()
        self.cat.delete_category()

    def test_update_method(self):
        """
        Function to test that a category's details can be updates
        """
        self.cat.save_category()
        new_cat = Category.objects.filter(name='this').update(name='hii')
        categories = Category.objects.get(name='hii')
        self.assertTrue(categories.name, 'hii')


class ImageTestClass(TestCase):
    """
    Tests Image class and its functions
    """
    #Set up method
    def setUp(self):
        #creating a new location and saving it
        self.locale = Location(name='hapa', description='testing')
        self.locale.save_location()

        #creating a new category and saving it
        self.cat = Category(name='this', description='testing1')
        self.cat.save_category()

        #creating an new image 
        self.image = Image(photo='test.jpg', name='name', description = 'this photo', location=self.locale, category = self.cat)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        """
        Function to test an image and its details is being saved
        """
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        """
        Function to test if an image can be deleted
        """
        self.image.save_image()
        self.image.delete_image()

    def test_filter_by_location(self):
        """
        Function to test if you can get an image by its location
        """
        self.image.save_image()
        this_img = self.image.filter_by_location(self.image.location)
        image = Image.objects.filter(location=self.image.location)
        self.assertTrue(this_img, image)

    def test_filter_by_category_name(self):
        """
        Function to test if you can get an image by its category name
        """
        self.image.save_image()
        images = Image.search_image('this')
        self.assertTrue(len(images)>0)

    
