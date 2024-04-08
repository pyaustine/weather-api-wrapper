import requests

class WeatherClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/"

    def get_current_weather(self, city):
        url = f"{self.base_url}weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_weather_forecast(self, city):
        url = f"{self.base_url}forecast?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_historical_weather(self, city, start_date, end_date):
        url = f"{self.base_url}onecall/timemachine?lat={city['lat']}&lon={city['lon']}&start={start_date}&end={end_date}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_air_pollution(self, city):
        url = f"{self.base_url}air_pollution?lat={city['lat']}&lon={city['lon']}&appid={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_uv_index(self, city):
        url = f"{self.base_url}uvi?lat={city['lat']}&lon={city['lon']}&appid={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_weather_alerts(self, city):
        url = f"{self.base_url}weather/alerts?q={city}&appid={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
