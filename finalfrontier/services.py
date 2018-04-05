import requests

def get_iss_location():
    url = f'http://api.open-notify.org/iss-now.json'
    r=requests.get(url)
    json_response=r.json()
    return json_response['iss_position']