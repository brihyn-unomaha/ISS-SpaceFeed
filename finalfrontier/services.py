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

# Function get_astronauts currently on the ISS
def get_iss_project_update():
    url = f'https://blogs.nasa.gov/stationreport/feed/'
    reg = requests.get(url)
    soup = BeautifulSoup(reg.text)
    reg.text #// XML as a string
    #articles = soup.findAll('item')
    articles = soup.find('item')
    status_update = articles.find('description')
    #for article in articles:
    #    status_update .title = article.find('title')
    #    status_update.description = article.find('description')
    #    status_update.link = article.find('link')
    #    status_update.pubdate = article.find('pubDate')
    return(status_update)