import pytest

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def api_headers():
    return {
        'x-api-key': 'reqres-free-v1',
        'Content-Type': 'application/json'
    }

@pytest.fixture
def test_user():
    return {
        "name": "morpheus",
        "job": "leader",
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }