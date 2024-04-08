import unittest
import requests
from unittest.mock import patch
from weather_api_wrapper.weather_client import WeatherClient
from weather_api_wrapper.exceptions import WeatherAPIError

class TestWeatherClient(unittest.TestCase):
    @patch('weather_api_wrapper.weather_client.requests.get')
    def test_get_current_weather(self, mock_get):
        mock_response = requests.models.Response()
        mock_response.status_code = 200
        mock_response.json = lambda: {"coord": {"lon": -0.13, "lat": 51.51}, "weather": [{"main": "Clouds", "description": "overcast clouds"}], "main": {"temp": 10.5, "feels_like": 8.89, "humidity": 76}, "wind": {"speed": 6.69, "deg": 240}, "clouds": {"all": 99}}
        mock_get.return_value = mock_response

        client = WeatherClient(api_key="fake_api_key")
        data = client.get_current_weather(city="London")

        self.assertEqual(data['coord']['lon'], -0.13)
        self.assertEqual(data['coord']['lat'], 51.51)
        self.assertEqual(data['weather'][0]['main'], "Clouds")
        self.assertEqual(data['weather'][0]['description'], "overcast clouds")
        self.assertEqual(data['main']['temp'], 10.5)
        self.assertEqual(data['main']['feels_like'], 8.89)
        self.assertEqual(data['main']['humidity'], 76)
        self.assertEqual(data['wind']['speed'], 6.69)
        self.assertEqual(data['wind']['deg'], 240)
        self.assertEqual(data['clouds']['all'], 99)

    @patch('weather_api_wrapper.weather_client.requests.get')
    def test_get_weather_forecast(self, mock_get):
        mock_response = requests.models.Response()
        mock_response.status_code = 200
        mock_response.json = lambda: {"city": {"name": "London"}, "list": [{"main": {"temp": 10.5}, "weather": [{"main": "Clouds", "description": "overcast clouds"}]}]}
        mock_get.return_value = mock_response

        client = WeatherClient(api_key="fake_api_key")
        data = client.get_weather_forecast(city="London")

        self.assertEqual(data['city']['name'], "London")
        self.assertEqual(data['list'][0]['main']['temp'], 10.5)
        self.assertEqual(data['list'][0]['weather'][0]['main'], "Clouds")
        self.assertEqual(data['list'][0]['weather'][0]['description'], "overcast clouds")

    @patch('weather_api_wrapper.weather_client.requests.get')
    def test_get_historical_weather(self, mock_get):
        mock_response = requests.models.Response()
        mock_response.status_code = 200
        mock_response.json = lambda: {"hourly": [{"temp": 10.5, "weather": [{"main": "Clouds", "description": "overcast clouds"}]}]}
        mock_get.return_value = mock_response

        client = WeatherClient(api_key="fake_api_key")
        data = client.get_historical_weather(city={"lon": -0.13, "lat": 51.51}, start_date="1612147200", end_date="1612233600")

        self.assertEqual(data['hourly'][0]['temp'], 10.5)
        self.assertEqual(data['hourly'][0]['weather'][0]['main'], "Clouds")
        self.assertEqual(data['hourly'][0]['weather'][0]['description'], "overcast clouds")

if __name__ == '__main__':
    unittest.main()
