import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def _data():
    return {
        'url': 'http://localhost:3000/api/v1/',
        'api_key': os.environ.get("APIKey", ""),
    }


def test_get_ReturnsAllItemLines(_data):
    url = _data['url'] + 'item_lines'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_get_ReturnsItemLine1(_data):
    url = _data['url'] + 'item_lines/1'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_get_ReturnsItemLine100000(_data):
    url = _data['url'] + 'item_lines/100000'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404


def test_get_ReturnsItemLinesWithoutApiKey(_data):
    url = _data['url'] + 'item_lines'

    # Send a GET request to the API without an API key
    response = requests.get(url)

    status_code = response.status_code

    # Verify that the status code is 401 (Unauthorized)
    assert status_code == 401


def test_post_ItemLine999001GetsAddedWithFullBody(_data):
    url = _data['url'] + 'item_lines'

    body = {
        "id": 999001,
        "name": "Integration test line",
        "description": "Created by integration test",
        "created_at": "2025-08-01T15:30:26Z",
        "updated_at": "2025-08-01T15:30:26Z"
    }

    # Send a POST request to the API
    response = requests.post(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 201 (Created)
    assert status_code == 201


def test_post_ItemLine999002GetsAddedWithHalfBody(_data):
    url = _data['url'] + 'item_lines'

    body = {
        "id": 999002,
        "name": "Integration test line half body",
    }

    # Send a POST request to the API
    response = requests.post(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 400 (Bad Request)
    assert status_code == 400


def test_put_UpdatesItemLine1WithFullBody(_data):
    item_line_id = 1
    url = _data['url'] + f'item_lines/{item_line_id}'

    # Data to update the item line with
    body = {
        "id": item_line_id,
        "name": "Aardappelen, groente en fruit",
        "description": "Updated description",
        "created_at": "2025-08-01T15:30:26Z",
        "updated_at": "2025-08-02T10:00:00Z"
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_put_UpdatesItemLine1WithHalfBody(_data):
    item_line_id = 1
    url = _data['url'] + f'item_lines/{item_line_id}'

    # Data to update the item line with
    body = {
        "id": item_line_id,
        "name": "Aardappelen, groente en fruit",
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_put_UpdatesItemLine100000(_data):
    item_line_id = 100000
    url = _data['url'] + f'item_lines/{item_line_id}'

    body = {
        "id": item_line_id,
        "name": "does not exist",
        "description": "Updated description",
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404


def test_delete_DeletesItemLine999001(_data):
    item_line_id = 999001
    url = _data['url'] + f'item_lines/{item_line_id}'

    # Send a DELETE request to the API
    response = requests.delete(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_delete_DeletesItemLine100000(_data):
    item_line_id = 100000
    url = _data['url'] + f'item_lines/{item_line_id}'

    # Send a DELETE request to the API
    response = requests.delete(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404