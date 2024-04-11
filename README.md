# Weather API Wrapper

[![License](https://img.shields.io/github/license/pyaustine/weather-api-wrapper)](LICENSE)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyaustine/weather-api-wrapper)
![GitHub last commit](https://img.shields.io/github/last-commit/pyaustine/weather-api-wrapper)
![GitHub issues](https://img.shields.io/github/issues/pyaustine/weather-api-wrapper)
![GitHub pull requests](https://img.shields.io/github/issues-pr/pyaustine/weather-api-wrapper)

A Python wrapper for the OpenWeatherMap API, enabling easy access to weather data for any location.

## Installation

You can install the Weather API Wrapper using pip:

```bash
pip install weather-api-wrapper
```

## Features

- Provides a Python interface to interact with the OpenWeatherMap API.
- Retrieve current weather, weather forecast, historical weather data, air pollution data, UV index data, and weather alerts for a specified location.
- Command-line interface (CLI) for easy access to weather data.

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

# Get air pollution data for a specific city
air_pollution = client.get_air_pollution(city={'lat': 51.51, 'lon': -0.13})

# Get UV index data for a specific city
uv_index = client.get_uv_index(city={'lat': 51.51, 'lon': -0.13})

# Get weather alerts for a specific city
weather_alerts = client.get_weather_alerts(city='New York')
```

Replace `your_api_key` with your actual OpenWeatherMap API key.

## Command Line Interface (CLI)

You can also use the command-line interface to retrieve weather data:

```bash
weather-cli --api-key your_api_key London
```

Replace 'your_api_key' with your actual [OpenWeatherMap API key](https://openweathermap.org/api) and 'London' with the city for which you want to retrieve weather data.

The CLI supports the following commands:

- `weather-cli`: Fetches current weather data for a specified city.
- `weather-cli --api-key your_api_key --forecast London`: Fetches weather forecast data for a specified city.
- `weather-cli --api-key your_api_key --historical London --start-date 2024-04-01 --end-date 2024-04-07`: Fetches historical weather data for a specified city and date range.
- `weather-cli --api-key your_api_key --pollution London`: Fetches air pollution data for a specified city.
- `weather-cli --api-key your_api_key --uv London`: Fetches UV index data for a specified city.
- `weather-cli --api-key your_api_key --alerts London`: Fetches weather alerts for a specified city.

## Documentation

For detailed usage instructions and API documentation, please refer to the [documentation](https://github.com/pyaustine/weather-api-wrapper).

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue on GitHub. See the [Code of conduct](CODE_OF_CONDUCT.md) for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
