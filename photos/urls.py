from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    url(r'^today/$', views.photos_of_day, name = 'photosToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photos,name = 'pastPhotos')
      # url(r'^search/', views.search_results, name='search_results'),
    # url(r'^photos/(\d+)',views.Photos,name ='photos'),
    # url(r'^category/(\w+)',views.category_photos,name='category_list'),
    # url(r'^location/(\w+)',views.location_photos,name='location_list'), 
]