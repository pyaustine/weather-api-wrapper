# Weather API Wrapper

![GitHub](https://img.shields.io/github/license/pyaustine/weather-api-wrapper)

A Python wrapper for the OpenWeatherMap API, enabling easy access to weather data for any location.

## Installation

You can install the Weather API Wrapper using pip:

```bash
pip install weather-api-wrapper
```

## Usage

```python
from weather_api_wrapper import WeatherClient

# Initialize the WeatherClient with your OpenWeatherMap API key
client = WeatherClient(api_key='your_api_key')

# Get current weather for a specific city
current_weather = client.get_current_weather(city='London')

# Get weather forecast for a specific city
forecast = client.get_weather_forecast(city='New York')

# Get historical weather data for a specific city and date range
historical_data = client.get_historical_weather(city={'lat': 51.51, 'lon': -0.13}, start_date='2024-04-01', end_date='2024-04-07')
```
Replace 'your_api_key' with your actual OpenWeatherMap API key.
