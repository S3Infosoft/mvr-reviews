import requests
import json

AUTH_KEY = "" # Google Api Key From Google Cloud Platform
PLACE_ID = "ChIJ-SP1jCQO6jsRrhLfnRKZtAg" # PlaceID of Mango Valley Resort From https://google-developers.appspot.com/maps/documentation/javascript/examples/full/places-placeid-finder

def Get_place_ratings(place_id,key):
    __url__ = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        'placeid': place_id,
        'fields' : "reviews",
        'key': key
    }

    response = requests.get(__url__,params=params)
    place_details = json.loads(response.content)
    return place_details

