import unittest
from weather_api_wrapper.exceptions import WeatherAPIError, WeatherAPIClientError, WeatherAPIResponseError

class TestExceptions(unittest.TestCase):
    def test_weather_api_error(self):
        with self.assertRaises(WeatherAPIError):
            raise WeatherAPIError("Generic weather API error")

    def test_weather_api_client_error(self):
        with self.assertRaises(WeatherAPIClientError):
            raise WeatherAPIClientError("Invalid parameter")

    def test_weather_api_response_error(self):
        status_code = 404
        message = "City not found"
        with self.assertRaises(WeatherAPIResponseError) as context:
            raise WeatherAPIResponseError(status_code, message)
        self.assertEqual(context.exception.status_code, status_code)
        self.assertEqual(context.exception.message, message)

if __name__ == '__main__':
    unittest.main()
