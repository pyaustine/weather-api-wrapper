from weather_api_wrapper import WeatherClient
# Initialize the WeatherClient with your OpenWeatherMap API key
client = WeatherClient(api_key='your_key_here')
# Get current weather for a specific city
current_weather = client.get_current_weather(city='London')
print(current_weather)