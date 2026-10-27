import pytest
from api.client import ApiClient

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_client(base_url):
    return ApiClient(base_url)