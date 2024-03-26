import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CountriesSerializer
from .models import Countries
import requests


class CountryLanguageView(APIView):
    def post(self, request):
        api_key2 = os.getenv('API_KEY2')
        city_name = request.data.get('city_name')
        if not city_name:
            return Response({'error': 'City name is required.'}, status=status.HTTP_400_BAD_REQUEST)
        # Make a request to the external API to get the country code
        api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(city_name)
        response = requests.get(api_url, headers={'X-Api-Key': api_key2})
        if response.status_code == requests.codes.ok:
            json = response.json()
            country_code = json[0]['country']
            # Query your database to find the matching country based on the country code
            try:
                country = Countries.objects.get(country_code=country_code)
                serializer = CountriesSerializer(country)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Countries.DoesNotExist:
                return Response({'error': 'Country with specified code not found in the database.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Failed to fetch data from external API.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    def get(self, request, *args, **kwargs):
    
    # getting a list of all tasks
        tasks = Countries.objects.all()#filter(completed=False)
        # feed all tasks into serializer
        serializer = CountriesSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
