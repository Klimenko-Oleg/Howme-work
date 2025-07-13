import pytest
import requests

BASE_URL = "https://yougile.com/api-v2/"
API_KEY = ()


@pytest.fixture
def api_client():
    """Фикстура для создания HTTP-клиента с настройками."""
    session = requests.Session()
    session.headers.update({'Authorization': f'Bearer {API_KEY}'})
    return session


@pytest.fixture
def project_id():
    """Фикстура для получения ID существующего проекта."""
    return "135f5254-1b1b-4506-bc7e-8dcf8b2d21a4"
