from django.shortcuts import render
import os
import requests

# Create your views here.
def get_country(city_name):
    api_key2 = os.getenv('API_KEY2')
    api_url = f'https://api.api-ninjas.com/v1/city?name={city_name}'
    response = requests.get(api_url, headers={'X-Api-Key': {api_key2}})
    if response.status_code == 200:
        data_list = response.json()
        if data_list:
            # Assuming the first item in the list contains the city information
            city_info = data_list[0]
            return city_info.get('country')
        else:
            return None
    return None