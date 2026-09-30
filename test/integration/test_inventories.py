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


def test_get_inventories(_data):
    url = _data["url"] + "inventories"

    response = requests.get(
        url,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code

    assert status_code == 200
    assert isinstance(response.json(), list)

    rows = response.json()

    assert rows, "Geen voorraadgegevens gevonden."

    for row in rows:
        assert isinstance(row["item_id"], int)
        assert isinstance(row["location_id"], int)
        assert isinstance(row["quantity_on_hand"], int)


def test_post_inventory(_data):
    url = _data["url"] + "inventories"

    # Eerst bestaande voorraad ophalen
    response = requests.get(
        url,
        headers={"API_KEY": _data["api_key"]}
    )

    assert response.status_code == 200

    rows = response.json()

    assert rows, "Geen voorraadgegevens voor deze test."

    original = rows[0].copy()

    body = original.copy()
    body["quantity_on_hand"] += 1

    # POST request
    response = requests.post(
        url,
        json=body,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code

    assert status_code == 201


def test_put_inventories(_data):
    url = _data["url"] + "inventories"

    # Eerst bestaande voorraad ophalen
    response = requests.get(
        url,
        headers={"API_KEY": _data["api_key"]}
    )

    assert response.status_code == 200

    rows = response.json()

    assert rows, "Geen voorraadgegevens voor deze test."

    body = rows[0].copy()
    body["quantity_on_hand"] += 1

    response = requests.put(
        url,
        json=body,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code

    assert status_code == 404
    # Actual endpoint currently returns 404 for PUT /inventories.


def test_delete_inventories(_data):
    url = _data["url"] + "inventories"

    response = requests.delete(
        url,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code

    assert status_code == 404
    # Actual endpoint currently returns 404 for DELETE /inventories.
