import pytest
import requests
from .schemas import (
    UserListResponse,
    UserResponse,
    CreateUserResponse,
    UpdateUserResponse,
    RegisterResponse,
    ErrorResponse
)

def test_get_users_list(base_url, api_headers):
    response = requests.get(f"{base_url}/users?page=2", headers=api_headers)
    assert response.status_code == 200
    UserListResponse(**response.json())


def test_get_single_user(base_url, api_headers):
    response = requests.get(f"{base_url}/users/2", headers=api_headers)
    assert response.status_code == 200
    UserResponse(**response.json())


def test_create_user(base_url, api_headers, test_user):
    response = requests.post(
        f"{base_url}/users",
        json={"name": test_user["name"], "job": test_user["job"]},
        headers=api_headers
    )
    assert response.status_code == 201
    CreateUserResponse(**response.json())


def test_update_user(base_url, api_headers, test_user):
    response = requests.put(
        f"{base_url}/users/2",
        json={"name": test_user["name"], "job": test_user["job"]},
        headers=api_headers
    )
    assert response.status_code == 200
    UpdateUserResponse(**response.json())


def test_delete_user(base_url, api_headers):
    response = requests.delete(f"{base_url}/users/2", headers=api_headers)
    assert response.status_code == 204
    assert not response.content


def test_register_success(base_url, api_headers, test_user):
    response = requests.post(
        f"{base_url}/register",
        json={"email": test_user["email"], "password": test_user["password"]},
        headers=api_headers
    )
    assert response.status_code == 200, f"Failed with status {response.status_code}. Response: {response.text}"
    RegisterResponse(**response.json())


def test_register_failure(base_url, api_headers):
    response = requests.post(
        f"{base_url}/register",
        json={"email": "invalid@test.com"},
        headers=api_headers
    )
    assert response.status_code == 400, f"Expected 400, got {response.status_code}. Response: {response.text}"
    ErrorResponse(**response.json())


def test_user_in_list(base_url, api_headers):
    target_user = {
        "id": 7,
        "email": "michael.lawson@reqres.in",
        "first_name": "Michael",
        "last_name": "Lawson"
    }

    response = requests.get(f"{base_url}/users?page=2", headers=api_headers)
    users = UserListResponse(**response.json()).data

    assert any(
        user.id == target_user["id"] and
        user.email == target_user["email"] and
        user.first_name == target_user["first_name"]
        for user in users
    ), f"User {target_user} not found in the list"