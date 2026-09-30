import os

import pytest
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")


@pytest.fixture
def _data():
    return {
        "url": "http://localhost:3000/api/v1/",
        "api_key": API_KEY,
    }


def test_get_item_types(_data):
    url = _data["url"] + "item_types"

    response = requests.get(
        url,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code

    assert status_code == 200
    assert isinstance(response.json(), list)

    names = [item["name"] for item in response.json()]

    assert "Single" in names
    assert "Multipack" in names
    assert "Bulk/Crate" in names


def test_get_one_item_type(_data):
    url = _data["url"] + "item_types/1"

    response = requests.get(
        url,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code

    assert status_code == 200
    assert response.json()["id"] == 1


def test_get_missing_item_type(_data):
    url = _data["url"] + "item_types/9999"

    response = requests.get(
        url,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code

# Actual response is 200 OK with null.
# 404 Not Found would be more appropriate because the requested item type does not exist.
    assert status_code == 404


def test_get_item_type_with_letters(_data):
    url = _data["url"] + "item_types/abc"

    response = requests.get(
        url,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code
    # Actual response is 500 Internal Server Error.
# 400 Bad Request would be more appropriate because "abc" is not a valid numeric ID.
    assert status_code == 400


def test_get_without_api_key(_data):
    url = _data["url"] + "item_types"

    response = requests.get(url)

    status_code = response.status_code
    #  HTTP/1.0 401 Unauthorized
    assert status_code == 401


# POST
def test_post_item_type(_data):
    url = _data["url"] + "item_types"

    body = {
        "id": 9999,
        "name": "Integration test",
        "description": "Tijdelijk itemtype",
    }

    response = requests.post(
        url,
        json=body,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code

    assert status_code == 201

# PUT


def test_put_item_type(_data):
    item_type_id = 9999
    url = _data["url"] + f"item_types/{item_type_id}"

    body = {
        "id": item_type_id,
        "name": "testtype",
        "description": "itemtype",
    }

    response = requests.put(
        url,
        json=body,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code

    assert status_code == 200


def test_delete_item_type(_data):
    item_type_id = 9999
    url = _data["url"] + f"item_types/{item_type_id}"

    response = requests.delete(
        url,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code

    assert status_code == 200
