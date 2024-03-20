from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable



def do_geocode(address, attempt=1, max_attempts=5):
    geolocator = Nominatim(user_agent="my_weather_app_v1")
    try:
        return geolocator.geocode(address)
    except (GeocoderTimedOut, GeocoderUnavailable):
        if attempt <= max_attempts:
            return do_geocode(address, attempt=attempt+1)  # retry
        raise
city_name = input('Enter city :')  # replace with your city name
location = do_geocode(city_name)
if location:
    print(location.address)
    print((location.latitude, location.longitude))
    # Perform additional actions with `location` here
else:
    print(f"Location for '{city_name}' not found.")