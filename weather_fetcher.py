import requests

API_KEY = "8c4e24bc0de3d42b164339b4540825e1"
"""the receiver of the request"""
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

"""Defining query parameters"""
city = input('Enter a city name: ')
"""Building a URL similar to the base URl to send requests"""
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

"""sending a get request to the url to receive data"""
response_data = requests.get(request_url)

"""Checking for the success of the response"""
if response_data.status_code == 200:
    """since the data receiving will be in json format and 
    to receive it as a python dictionary"""
    data = response_data.json()
    weather =data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15,2) # to convert to celsius
    print(f"The weather: ",weather)
    print("Temperature: ",temperature, "celsius")
else:
    print('An error occurred')
