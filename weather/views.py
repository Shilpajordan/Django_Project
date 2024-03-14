from django.shortcuts import render
import requests
import os
# from dotenv import load_dotenv

# Create your views here.

"""the receiver of the request"""
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(request):
    if request.method == 'POST':
        api_key = os.getenv('API_KEY')
        city = request.POST.get('city')
        request_url = f"{BASE_URL}?appid={api_key}&q={city}"
        response_data = requests.get(request_url)
        if response_data.status_code == 200:
            data = response_data.json()
            weather = data['weather'][0]['description']
            temperature = round(data['main']['temp'] - 273.15, 2)
            return render(request, 'weather/weather.html', {'weather': weather, 'temperature': temperature})
        else:
            error_message = 'An error occurred'
            return render(request, 'weather/error.html', {'error_message': error_message})
    return render(request, 'weather/form.html')