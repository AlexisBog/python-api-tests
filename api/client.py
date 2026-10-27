import logging
import requests

# Налаштування логування для консолі
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.logger = logging.getLogger("ApiClient")

    def make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"Sending {method} request to -> {url}")
        if "json" in kwargs:
            self.logger.info(f"Request payload: {kwargs['json']}")
        if "params" in kwargs:
            self.logger.info(f"Request query params: {kwargs['params']}")

        response = requests.request(method, url, **kwargs)
        
        self.logger.info(f"Response status: {response.status_code}")
        try:
            self.logger.info(f"Response body: {response.json()}")
        except ValueError:
            self.logger.info(f"Response body (text): {response.text}")
            
        return response

    def get(self, endpoint, **kwargs):
        return self.make_request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.make_request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.make_request("PUT", endpoint, **kwargs)

    def patch(self, endpoint, **kwargs):
        return self.make_request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.make_request("DELETE", endpoint, **kwargs)