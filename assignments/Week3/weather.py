import requests

API_KEY = 'your_api_key_here'  # Hidden my API key for security reasons
CITY = input("Enter City Name: ")  
UNITS = 'metric'  
url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed']
    }
    print(f"Weather in {weather['city']}:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Condition: {weather['description']}")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind Speed: {weather['wind_speed']} m/s")
else:
    print(f"Error {response.status_code}: {response.text}")