import os
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Countries
from .serializers import CountriesSerializer


class YourView(APIView):
    def get_code(self, city_name):
        api_key2 = os.getenv('API_KEY2')
        api_url = f'https://api.api-ninjas.com/v1/city?name={city_name}'
        response = requests.get(api_url, headers={'X-Api-Key': api_key2})
        if response.status_code == 200:
            data_list = response.json()
            if data_list:
                # Assuming the first item in the list contains the city information
                city_info = data_list[0]
                return city_info.get('country')
        return None
    def get(self, request, city_name):
        country_code = self.get_code(city_name)
        if country_code:
            try:
                country = Countries.objects.get(country_code=country_code)
                serializer = CountriesSerializer(country)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Countries.DoesNotExist:
                return Response({'message': 'Country not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'City not found'}, status=status.HTTP_404_NOT_FOUND)