import requests
import json
import urllib.request
from bs4 import BeautifulSoup
import feedparser
import ast

# Function get_iss_location gets the current location of the ISS as a comobined lat/lon json
def get_iss_location():
    url = f'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result= json.loads(response.read())
    location = result['iss_position']
    return(location)

# Function get_astronauts currently on the ISS
def get_astronauts():
    getresp = f'http://api.open-notify.org/astros.json'
    request = requests.get(getresp)
    requester = request.json()
    dump = json.dumps(requester)
    result= json.loads(dump)
    spacecadets = result['people']
    #spacestr = ''.join(spacecadets)
    #a, cleanup = spacestr.split('[', 2)
    #cleanup2, b = spacestr.split(']', 2)
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
    a, b, cleanup = status_update.split('[', 3)
    cleanup2, d = cleanup.split('&', 2)
    return(cleanup2)

def get_NASA_IOTD():
    url = f'https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss'
    feedurl = feedparser.parse(url)
    iotd_Url = feedurl.entries[00].links[1].href
    return (iotd_Url)