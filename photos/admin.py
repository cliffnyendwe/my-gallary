from django.contrib import admin
from .models import location,categorys,Image

# my models are regestered here.

admin.site.register(location)
admin.site.register(Image)
admin.site.register(categorys)
