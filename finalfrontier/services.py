import requests
import json
import urllib.request
from bs4 import BeautifulSoup

# Function get_iss_location gets the current location of the ISS as a comobined lat/lon json
def get_iss_location():
    url = f'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result= json.loads(response.read())
    location = result['iss_position']
    return(location)

# Function get_astronauts currently on the ISS
def get_astronauts():
    url = f'http://api.open-notify.org/astros.json'
    response = urllib.request.urlopen(url)
    result= json.loads(response.read())
    spacecadets = result['people']
    return(spacecadets)

# Function get_NASA current daily project update
def get_iss_project_update():
    url = f'https://blogs.nasa.gov/stationreport/feed/'
    reg = requests.get(url)
    soup = BeautifulSoup(reg.text)
    articles = soup.findAll('item')
    for article in articles:
        status_update = article.find('description')
        status_update = str(status_update) #switch the output to a string
        break #couldn't figure out how to get only the latest RSS update, so this would loop through all...but we break after the first.
    return(status_update)