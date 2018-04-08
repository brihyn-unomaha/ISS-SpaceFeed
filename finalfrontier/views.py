from django.shortcuts import render, get_object_or_404
from .models import Space
from.services import get_iss_location


def home(request):
    #We're combining all of the data into a class named Space as attributes.

    #ISS Data Retrieval
    #Call the Services.py file function to get the various space data
    Space.location = get_iss_location()
    # Separate out the individual latitude and longitude
    Space.lat=Space.location['latitude']
    Space.lon = Space.location['longitude']

    #NASA RSS Feed retrieval for Project Status

    #NASA Twitter Feed

    #Creating image of Earth with ISS Positioned on it.

    # Send the Space class to the html page
    return render(request, 'finalfrontier/home.html', {'Space': Space})

