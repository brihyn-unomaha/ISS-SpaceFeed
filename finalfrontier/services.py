import requests
import json
import urllib.request

# Function get_iss_location gets the current location of the ISS as a comobined lat/lon json
def get_iss_location():
    url = f'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result= json.loads(response.read())
    location = result['iss_position']
    return(location)
