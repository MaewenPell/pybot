import os

MAPS_API_KEY_FRONT = "AIzaSyD8uuCHTvgUkUPDQc8W8Ae4MQ2sMzw1I1Y"

if os.environ.get('MAPS_API_KEY') is not None:
    MAPS_API_KEY = os.environ.get('MAPS_API_KEY')
else:
    MAPS_API_KEY = "YOUR API KEY HERE"
