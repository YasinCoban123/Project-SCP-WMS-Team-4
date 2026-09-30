import pytest
import requests


@pytest.fixture
def _data():
    return {
        'url': 'http://localhost:3000/api/v1/',
        'api_key': 's1h3i5p7p9i2n4g6s8t',
    }


def test_get_return_all_shipments(_data):
    url = _data['url'] + 'shipments'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    # Get the status code and response data
    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_post_Shipment2016GetsAddedWithFullBody(_data):
    url = _data['url'] + 'shipments'

    body = {
        "id": 2016,
        "reference": "SHP-002016",
        "order_id": 1,
        "shipment_date": "2026-06-21T22:43:23Z",
        "shipment_type": "Outgoing",
        "shipment_status": "Scheduled",
        "carrier_name": "DHL Parcel",
        "shipping_method": "Standard",
        "payment_type": "Automated",
        "created_at": "2026-06-21T22:43:23Z",
        "updated_at": "2026-06-23T04:51:45Z",
    }

    # Send a POST request to the API
    response = requests.post(url, json=body, headers={'API_KEY': _data['api_key']})

    # Verify that the status code is 201 (Created)
    assert response.status_code == 201


def test_put_UpdatesShipment2WithFullBody(_data):
    shipment_id = 2
    url = _data['url'] + f'shipments/{shipment_id}'

    body = {
        "id": shipment_id,
        "reference": "SHP-000002-UPDATED",
        "order_id": 3,
        "shipment_date": "2026-08-09T13:21:23Z",
        "shipment_type": "Outgoing",
        "shipment_status": "Transit",
        "carrier_name": "PostNL",
        "shipping_method": "Express",
        "payment_type": "Automated",
        "created_at": "2025-08-09T13:21:23Z",
        "updated_at": "2025-08-10T21:49:56Z",
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    # Verify that the status code is 200 (OK)
    assert response.status_code == 200


def test_delete_DeletesNonExistentShipment10000(_data):
    shipment_id = 10000
    url = _data['url'] + f'shipments/{shipment_id}'

    # Send a DELETE request to the API
    response = requests.delete(url, headers={'API_KEY': _data['api_key']})

    # Verify that the status code is 404 (Not Found)
    assert response.status_code == 404