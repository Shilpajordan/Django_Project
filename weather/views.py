from django.shortcuts import render
import requests
import os
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable

# # Create your views here.

# """the receiver of the request"""
# BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# def get_weather(request):
#     if request.method == 'POST':
#         api_key = os.getenv('API_KEY')
#         city = request.POST.get('city')
#         request_url = f"{BASE_URL}?appid={api_key}&q={city}"
#         response_data = requests.get(request_url)
#         if response_data.status_code == 200:
#             data = response_data.json()
#             weather = data['weather'][0]['description']
#             temperature = round(data['main']['temp'] - 273.15, 2)
#             return render(request, 'weather/weather.html', {'weather': weather, 'temperature': temperature})
#         else:
#             error_message = 'An error occurred'
#             return render(request, 'weather/error.html', {'error_message': error_message})
#     return render(request, 'weather/form.html')


# def do_geocode(address, attempt=1, max_attempts=5):
#     geolocator = Nominatim(user_agent="my_weather_app_v1")
#     try:
#         return geolocator.geocode(address)
#     except (GeocoderTimedOut, GeocoderUnavailable):
#         if attempt <= max_attempts:
#             return do_geocode(address, attempt=attempt+1)  # retry
#         raise
# city_name = input('Enter city :')  # replace with your city name
# location = do_geocode(city_name)
# if location:
#     print(location.address)
#     print((location.latitude, location.longitude))
#     # Perform additional actions with `location` here
# else:
#     print(f"Location for '{city_name}' not found.")

# Constants
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
# Function to get country information for a city
def get_country(city_name):
    geolocator = Nominatim(user_agent="my_weather_app_v1")
    location = geolocator.geocode(city_name)
    if location:
        return location.address.split(",")[-1].strip()
    else:
        return None
# View to get weather and country information
def get_weather(request):
    if request.method == 'POST':
        api_key = os.getenv('API_KEY')
        city = request.POST.get('city')
        # Retrieve weather information
        request_url = f"{BASE_URL}?appid={api_key}&q={city}"
        response_data = requests.get(request_url)
        if response_data.status_code == 200:
            weather_data = response_data.json()
            weather = weather_data['weather'][0]['description']
            temperature = round(weather_data['main']['temp'] - 273.15, 2)
            # Retrieve country information
            country = get_country(city)
            if country:
                return render(request, 'weather/weather.html', {'weather': weather, 'temperature': temperature, 'country': country})
            else:
                error_message = f'Country information for {city} not found'
                return render(request, 'weather/error.html', {'error_message': error_message})
        else:
            error_message = 'City not found'
            return render(request, 'weather/error.html', {'error_message': error_message})
    return render(request, 'weather/form.html')