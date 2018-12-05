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
        return self.name

    class Meta:
        ordering = ['name']

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Image(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    location = models.ForeignKey(location)
    category = models.ManyToManyField(Categorys, default = True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    Image_image = models.ImageField(upload_to = 'images/')

    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    