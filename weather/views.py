from django.shortcuts import render
import requests
import os
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable

# # Create your views here.


# Constants
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to get country information for a city
def get_country(city_name):
    api_url = 'http://127.0.0.1:8000/api/country-language/' 
    response = requests.post(api_url, json={'city_name': city_name})
    if response.status_code == 200:
        data = response.json()
        country_name = data.get('country_name')
        language = data.get('language')
        return country_name, language
    else:
        return None, None
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