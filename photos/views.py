
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import location,Categorys,Photo

# Create your views here.
def photos_today(request):
    date = dt.date.today()
    photos = Photo.todays_photos()
    return render(request, 'all-photos/today-photos.html',{'date': date,"photos":photos})



def past_days_photos(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(location_today)
    
    photos = Photo.todays_photos()
    return render(request, 'all-photos/past-photos.html', {"date":date,"photos":photos})