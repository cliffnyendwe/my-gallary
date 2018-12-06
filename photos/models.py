from django.db import models
import datetime as dt

# Create your models here.
class location(models.Model):
    location = models.CharField(max_length =40)
  
    def __str__(self):
        return self.location_name
    class meta:
        ordering =['location']
    
    def save_location(self):
        self.save()


class Categorys(models.Model):
    Category = models.CharField(max_length =40)
   

    def __str__(self):
        return self.title


class Photo(models.Model):
    photo = models.ImageField(upload_to = 'photos/')
    location =models.ForeignKey(location)
    category =models.ManyToManyField(Categorys, default = True)
    post_date =models.DateTimeField(auto_now_add=True, null=True) 
 
    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        photos = cls.objects.filter(post_date = today)
        return photos
    
    @classmethod
    def days_photos(cls,date):
        photos = cls.objects.filter(post_date = date)
        return photos