class WeatherAPIError(Exception):
    """Base class for exceptions in the weather API wrapper."""
    pass

class WeatherAPIClientError(WeatherAPIError):
    """Exception raised for errors in the weather API client."""
    pass

class WeatherAPIResponseError(WeatherAPIError):
    """Exception raised for errors in the weather API response."""
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"Received unexpected status code {status_code}: {message}")