from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Space
from.services import get_iss_location


def home(request):
    #space = get_object_or_404(Space)
    Space.location = get_iss_location()
    Space.lat=Space.location['latitude']
    Space.lon = Space.location['longitude']
    return render(request, 'finalfrontier/home.html', {'Space': Space})

