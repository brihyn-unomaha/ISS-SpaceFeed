from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Space
from.services import get_iss_location


def home(request):
    #space = get_object_or_404(Space)
    Space.iss_current_location = get_iss_location()
    return render(request, 'finalfrontier/home.html', {'space': Space})

