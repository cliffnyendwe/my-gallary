from django.shortcuts import render
import datetime as dt
# Create your views here.
from django.http import HttpResponse

# create my views here


def welcome(request):
    return HttpResponse('Welcome to my Gallary')


def photos_of_day(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> Photos for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
        '''
    return HttpResponse(html)
def convert_dates(dates):
    #functions that gets the weekday number for the date.

    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    # returning the actual day of the week

    day = days[day_number]
    return day