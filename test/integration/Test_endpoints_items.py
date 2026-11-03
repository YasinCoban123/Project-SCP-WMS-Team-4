import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def _data():
    return {
        'url': 'http://localhost:3000/api/v1/',
        'api_key': "f4a5c6i7l8i9t0y1m2a3n4a5g6",
    }


def test_get_ReturnsAllItems(_data):
    url = _data['url'] + 'items'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_get_ReturnsItem1(_data):
    url = _data['url'] + 'items/1'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_get_ReturnsItem999999(_data):
    url = _data['url'] + 'items/999999'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404


def test_get_ReturnsItemsWithoutApiKey(_data):
    url = _data['url'] + 'items'

    # Send a GET request to the API without an API key
    response = requests.get(url)

    status_code = response.status_code

    # Verify that the status code is 401 (Unauthorized)
    assert status_code == 401


def test_post_Item999001GetsAddedWithFullBody(_data):
    url = _data['url'] + 'items'

    body = {
        "id": 999001,
        "name": "Integration Test Item",
        "description": "Created by integration test",
    }

    # Send a POST request to the API
    response = requests.post(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 201 (Created)
    assert status_code == 201


def test_post_Item999002GetsAddedWithHalfBody(_data):
    url = _data['url'] + 'items'

    body = {
        "id": 999002,
        "name": "Integration Test Item half body",
    }

    # Send a POST request to the API
    response = requests.post(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 400 (Bad Request)
    assert status_code == 400


def test_put_UpdatesItem999001WithFullBody(_data):
    item_id = 999001
    url = _data['url'] + f'items/{item_id}'

    # Data to update the item with
    body = {
        "id": item_id,
        "name": "Aangepaste naam",
        "description": "Nieuwe beschrijving",
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_put_UpdatesItem999001WithHalfBody(_data):
    item_id = 999001
    url = _data['url'] + f'items/{item_id}'

    # Data to update the item with
    body = {
        "id": item_id,
        "name": "Updated Integration Test Item",
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_put_UpdatesItem999999(_data):
    item_id = 999999
    url = _data['url'] + f'items/{item_id}'

    body = {
        "id": item_id,
        "name": "does not exist",
        "description": "Nieuwe beschrijving",
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404


def test_get_ReturnsInventoryOfItem999001(_data):
    url = _data['url'] + 'items/999001/inventory'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_get_ReturnsInventoryTotalsOfItem999001(_data):
    url = _data['url'] + 'items/999001/inventory/totals'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_delete_DeletesItem999001(_data):
    item_id = 999001
    url = _data['url'] + f'items/{item_id}'

    # Send a DELETE request to the API
    response = requests.delete(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_delete_DeletesItem999999(_data):
    item_id = 999999
    url = _data['url'] + f'items/{item_id}'

    # Send a DELETE request to the API
    response = requests.delete(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404