
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import categorys,Image,location

# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def photos_of_day(request):
    date = dt.date.today()
    photos = Photos.gallery_photos()
    category= categorys.objects.all()
    location= location.objects.all()
    return render(request,'all-photos/gallary-photos.html',{"photos":photos,'category':category,"location":location})

def past_days_photos(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_of_day)

    return render(request, 'all-photos/past-photos.html', {"date":date})

    try:
        location = location.objects.get(email = 'location')
        print('location found')
    except DoesNotExist:
        print('location was not found')

    
def search_results(request):
    category= categorys.objects.all()
    location= location.objects.all()
    if 'photos' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photos")
        searched_photos = Photos.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"photos": searched_photos,'category':category,"location":location})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})