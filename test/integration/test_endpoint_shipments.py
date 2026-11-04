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


def test_post_Shipment999903GetsAddedWithFullBody(_data):
    url = _data['url'] + 'shipments'

    body = {
        "id": 999903,
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


def test_get_shipments_without_api_key_returns_401(_data):
    url = _data['url'] + 'shipments'

    response = requests.get(url)

    assert response.status_code == 401


def test_post_shipments_without_api_key_returns_401(_data):
    url = _data['url'] + 'shipments'

    response = requests.post(url, json={})

    assert response.status_code == 401


def test_post_shipments_with_invalid_api_key_returns_401(_data):
    url = _data['url'] + 'shipments'

    response = requests.post(url, json={}, headers={'API_KEY': 'invalid-key'})

    assert response.status_code == 401


def test_post_shipment_route_without_api_key_returns_401(_data):
    url = _data['url'] + 'shipments/1'

    response = requests.post(url, json={})

    assert response.status_code == 401


def test_put_shipment_without_api_key_returns_401(_data):
    url = _data['url'] + 'shipments/1'

    response = requests.put(url, json={})

    assert response.status_code == 401


def test_put_shipment_with_invalid_api_key_returns_401(_data):
    url = _data['url'] + 'shipments/1'

    response = requests.put(url, json={}, headers={'API_KEY': 'invalid-key'})

    assert response.status_code == 401


def test_delete_shipment_without_api_key_returns_401(_data):
    url = _data['url'] + 'shipments/1'

    response = requests.delete(url)

    assert response.status_code == 401


def test_delete_shipment_with_invalid_api_key_returns_401(_data):
    url = _data['url'] + 'shipments/1'

    response = requests.delete(url, headers={'API_KEY': 'invalid-key'})

    assert response.status_code == 401


def test_get_shipments_with_invalid_api_key_returns_401(_data):
    url = _data['url'] + 'shipments'

    response = requests.get(url, headers={'API_KEY': 'invalid-key'})

    assert response.status_code == 401


def test_post_shipment_route_with_invalid_api_key_returns_401(_data):
    url = _data['url'] + 'shipments/1'

    response = requests.post(url, json={}, headers={'API_KEY': 'invalid-key'})

    assert response.status_code == 401


def test_put_shipment_items_without_api_key_returns_401(_data):
    url = _data['url'] + 'shipments/1/items'

    response = requests.put(url, json={})

    assert response.status_code == 401


def test_delete_unknown_shipment_without_api_key_returns_401(_data):
    url = _data['url'] + 'shipments/10000'

    response = requests.delete(url)

    assert response.status_code == 401


def test_get_shipment_returns_expected_data(_data):
    response = requests.get(
        _data['url'] + 'shipments/1',
        headers={'API_KEY': _data['api_key']},
    )

    assert response.status_code == 200
    shipment = response.json()
    assert shipment['id'] == 1
    assert shipment['reference']
    assert shipment['order_id'] == 1
    assert isinstance(shipment['items'], list)


def test_get_shipments_returns_non_empty_list(_data):
    response = requests.get(
        _data['url'] + 'shipments',
        headers={'API_KEY': _data['api_key']},
    )

    assert response.status_code == 200
    shipments = response.json()
    assert isinstance(shipments, list)
    assert shipments
    assert any(shipment['id'] == 1 for shipment in shipments)
    assert all(isinstance(shipment['items'], list) for shipment in shipments)


def test_post_shipment_can_be_retrieved_after_creation(_data):
    shipment = {
        'id': 999901,
        'reference': 'SHP-INTEGRATION-001',
        'order_id': 1,
        'shipment_date': '2026-11-03T20:00:00Z',
        'shipment_type': 'Outgoing',
        'shipment_status': 'Scheduled',
        'carrier_name': 'DHL Parcel',
        'shipping_method': 'Standard',
        'payment_type': 'Automated',
    }

    create_response = requests.post(
        _data['url'] + 'shipments',
        headers={'API_KEY': _data['api_key']},
        json=shipment,
    )
    get_response = requests.get(
        _data['url'] + 'shipments/999901',
        headers={'API_KEY': _data['api_key']},
    )

    assert create_response.status_code == 201
    assert get_response.status_code == 200
    assert get_response.json()['reference'] == shipment['reference']
    assert get_response.json()['shipment_status'] == shipment['shipment_status']


def test_put_shipment_changes_persisted_data(_data):
    shipment = {
        'id': 2,
        'reference': 'SHP-INTEGRATION-UPDATED',
        'order_id': 3,
        'shipment_date': '2026-11-04T20:00:00Z',
        'shipment_type': 'Outgoing',
        'shipment_status': 'Delivered',
        'carrier_name': 'PostNL',
        'shipping_method': 'Express',
        'payment_type': 'Manual',
    }

    update_response = requests.put(
        _data['url'] + 'shipments/2',
        headers={'API_KEY': _data['api_key']},
        json=shipment,
    )
    get_response = requests.get(
        _data['url'] + 'shipments/2',
        headers={'API_KEY': _data['api_key']},
    )

    assert update_response.status_code == 200
    assert get_response.status_code == 200
    updated_shipment = get_response.json()
    assert updated_shipment['id'] == 2
    assert updated_shipment['reference'] == shipment['reference']
    assert updated_shipment['shipment_status'] == shipment['shipment_status']


def test_delete_shipment_removes_it_from_api(_data):
    shipment = {
        'id': 999902,
        'reference': 'SHP-INTEGRATION-DELETE',
        'order_id': 1,
        'shipment_date': '2026-11-05T20:00:00Z',
        'shipment_type': 'Incoming',
        'shipment_status': 'Scheduled',
        'carrier_name': 'GLS',
        'shipping_method': 'Standard',
        'payment_type': 'Manual',
    }

    create_response = requests.post(
        _data['url'] + 'shipments',
        headers={'API_KEY': _data['api_key']},
        json=shipment,
    )
    delete_response = requests.delete(
        _data['url'] + 'shipments/999902',
        headers={'API_KEY': _data['api_key']},
    )
    get_response = requests.get(
        _data['url'] + 'shipments/999902',
        headers={'API_KEY': _data['api_key']},
    )

    assert create_response.status_code == 201
    assert delete_response.status_code == 200
    assert get_response.status_code == 404


def test_get_shipment_orders_returns_expected_order(_data):
    response = requests.get(
        _data['url'] + 'shipments/1/orders',
        headers={'API_KEY': _data['api_key']},
    )

    assert response.status_code == 200
    order_ids = response.json()
    assert isinstance(order_ids, list)
    assert order_ids == [1]