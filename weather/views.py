from django.shortcuts import render
import requests
import os

# Constants
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_country(city):
    api_url = 'http://127.0.0.1:8000/api/country-language/'
    response = requests.post(api_url, json={'city_name': city})

    if response.status_code == 200:
        return response.json()
    else:
        return None
    

def get_weather(request):
    if request.method == 'POST':
        api_key = os.getenv('API_KEY')
        city = request.POST.get('city')
        request_url = f"{BASE_URL}?appid={api_key}&q={city}"
        response_data = requests.get(request_url)
        
        if response_data.status_code == 200:
            weather_data = response_data.json()
            weather = weather_data['weather'][0]['description']
            temperature = round(weather_data['main']['temp'] - 273.15, 2)
            country_data = get_country(city)
            
            if country_data:
                country_name = country_data.get('country_name')
                language = country_data.get('language')
                return render(request, 'weather/weather.html', {'weather': weather, 'temperature': temperature, 'country': country_name, 'language': language})
            else:
                error_message = f'Country information for {city} not found'
                return render(request, 'weather/error.html', {'error_message': error_message})
        else:
            error_message = 'City not found'
            return render(request, 'weather/error.html', {'error_message': error_message})
    return render(request, 'weather/form.html')