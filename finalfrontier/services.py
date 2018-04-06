import requests
import json
import urllib.request
#from .models import Space

# Function get_iss_location gets the current location of the ISS, and adds to three attributes, locaiton (combined lat/lon), lat, and lon
def get_iss_location():
    url = f'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result= json.loads(response.read())
    location = result['iss_position']
    #Space.lat=Space.location['latitude']
    #Space.lon=Space.location['longitude']
    return(location)
