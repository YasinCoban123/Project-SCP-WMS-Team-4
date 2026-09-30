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


def test_get_order(_data):
    url = _data["url"] + "orders/1"

    response = requests.get(
        url,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code

    assert status_code == 200
    assert response.json()["id"] == 1
    assert isinstance(response.json()["items"], list)


def test_get_missing_order(_data):
    url = _data["url"] + "orders/9999"

    response = requests.get(
        url,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code

    assert status_code == 404


def test_get_order_with_letters(_data):
    url = _data["url"] + "orders/abc"

    response = requests.get(
        url,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code

    assert status_code == 400


def test_post_order(_data):
    url = _data["url"] + "orders"

    body = {
        "id": 9999,
        "client_id": 123,
        "order_date": "2026-09-29T10:00:00Z",
        "request_date": "2026-10-01T10:00:00Z",
        "reference": "TEST-9999",
        "customer_po_number": "TEST-PO",
        "order_status": "Pending",
        "shipping_notes": "Testorder",
        "warehouse_id": 2,
        "ship_to_client_id": 31,
        "bill_to_client_id": 87,
        "items": [
            {
                "item_id": 82,
                "amount": 1
            }
        ],
    }

    response = requests.post(
        url,
        json=body,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code

    assert status_code == 201


def test_put_order(_data):
    order_id = 9999
    url = _data["url"] + f"orders/{order_id}"

    body = {
        "id": order_id,
        "client_id": 123,
        "order_date": "2026-09-29T10:00:00Z",
        "request_date": "2026-10-01T10:00:00Z",
        "reference": "TEST-9999",
        "customer_po_number": "TEST-PO",
        "order_status": "Pending",
        "shipping_notes": "Gewijzigd",
        "warehouse_id": 2,
        "ship_to_client_id": 31,
        "bill_to_client_id": 87,
        "items": [
            {
                "item_id": 82,
                "amount": 1
            }
        ],
    }

    response = requests.put(
        url,
        json=body,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code

    assert status_code == 200


def test_delete_order(_data):
    order_id = 9999
    url = _data["url"] + f"orders/{order_id}"

    response = requests.delete(
        url,
        headers={"API_KEY": _data["api_key"]}
    )

    status_code = response.status_code

    assert status_code == 200
