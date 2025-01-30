import requests

city = input('Which city: ')

url = "http://api.openweathermap.org/data/2.5/weather"
url += "?appid=d1526a9039658a6f76950cff21823aff"
url += "&units=metric"
url += "&mode=json"
url += "&q=" + city

print(url)

response = requests.get(url)

data = response.json()

temperature = data['main']['temp']
feels_like = data['main']['feels_like']

print(f'It is {temperature} degrees in {city} but that feels like {feels_like} degrees.')
