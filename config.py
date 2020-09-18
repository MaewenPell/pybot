import os

if os.environ.get('MAPS_API_KEY') is not None:
    MAPS_API_KEY = os.environ.get('MAPS_API_KEY')
else:
    MAPS_API_KEY = "API_KEY_HERE"
