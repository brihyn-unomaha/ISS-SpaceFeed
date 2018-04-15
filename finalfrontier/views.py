from django.shortcuts import render, get_object_or_404
from .models import Space
from.services import get_iss_location, get_astronauts, get_iss_project_update, get_NASA_IOTD


def home(request):
    #We're combining all of the data into a class named Space as attributes.

    #ISS Data Retrieval
    #Call the Services.py file function to get the various space data
    Space.location = get_iss_location()
    # Separate out the individual latitude and longitude
    Space.lat=Space.location['latitude']
    Space.lon = Space.location['longitude']

    # Call the Services.py file function to get the various space data
    Space.cadets = get_astronauts()
    Space.spacecadets = []
    for p in Space.cadets:
        Space.spacecadets.append(p['name'])

    #NASA RSS Feed retrieval for Project Status
    Space.status_update = get_iss_project_update()

    #NASA RSS Feed retreival for Image of the Day
    Space.daily_image = get_NASA_IOTD()

    #NASA Twitter Feed

    #Creating image of Earth with ISS Positioned on it.

    # Send the Space class to the html page
    return render(request, 'finalfrontier/home.html', {'Space': Space})

