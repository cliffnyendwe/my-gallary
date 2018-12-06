from django.db import models

# Create your models here.

class location(models.Model):
    location = models.CharField(max_length=40)

    def __str__(self):
        return self.location_name

    
    class Meta:
        ordering = ['location']

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    
# Create my model class for category here.
class categorys(models.Model):
    categorys = models.CharField(max_length =40)

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ['category']

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Image(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    location = models.ForeignKey(location)
    categorys = models.ManyToManyField(categorys, default = True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    Image_image = models.ImageField(upload_to = 'images/')

    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['image']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__name__icontains=search_term)
        return photos

    @classmethod
    def get_by_location(cls,search_term):
        photos = cls.objects.filter(location__name__icontains=search_term)
        return photos

    