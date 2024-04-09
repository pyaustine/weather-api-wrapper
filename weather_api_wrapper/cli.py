import argparse
from .weather_client import WeatherClient

def main():
    parser = argparse.ArgumentParser(description='Weather CLI')
    parser.add_argument('city', type=str, help='City name')
    parser.add_argument('--api-key', type=str, required=True, help='OpenWeatherMap API key')

    args = parser.parse_args()

    client = WeatherClient(api_key=args.api_key)

    try:
        weather_data = client.get_current_weather(city=args.city)
        print("Current Weather:")
        print(weather_data)
    except Exception as e:
        print(f"Error fetching weather data: {e}")

    try:
        forecast_data = client.get_weather_forecast(city=args.city)
        print("\nWeather Forecast:")
        print(forecast_data)
    except Exception as e:
        print(f"Error fetching weather forecast: {e}")

    try:
        historical_data = client.get_historical_weather(city=args.city, start_date='2024-04-01', end_date='2024-04-07')
        print("\nHistorical Weather:")
        print(historical_data)
    except Exception as e:
        print(f"Error fetching historical weather data: {e}")

    try:
        air_pollution_data = client.get_air_pollution(city=args.city)
        print("\nAir Pollution Data:")
        print(air_pollution_data)
    except Exception as e:
        print(f"Error fetching air pollution data: {e}")

    try:
        uv_index_data = client.get_uv_index(city=args.city)
        print("\nUV Index Data:")
        print(uv_index_data)
    except Exception as e:
        print(f"Error fetching UV index data: {e}")

    try:
        weather_alerts = client.get_weather_alerts(city=args.city)
        print("\nWeather Alerts:")
        print(weather_alerts)
    except Exception as e:
        print(f"Error fetching weather alerts: {e}")

if __name__ == '__main__':
    main()
