import pytest
import requests


@pytest.fixture
def _data():
    return {
        'url': 'http://localhost:3000/api/v1/',
        'api_key': 'f4a5c6i7l8i9t0y1m2a3n4a5g6',
    }


def test_get_ReturnAllTransfers(_data):
    url = _data['url'] + 'transfers'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    # Get the status code and response data
    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200

def test_get_ReturnsTransfer10000(_data):
    url = _data['url'] + 'transfers/10000'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    # Get the status code and response data
    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404

def test_get_ReturnsTransfer1(_data):
    url = _data['url'] + 'transfers/1'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    # Get the status code and response data
    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_post_Transfer2016GetsAddedWithFullBody(_data):
    url = _data['url'] + 'transfers'

    body = {
        "id": 2016,
        "reference": "TRF-002016",
        "from_location_id": 1,
        "to_location_id": 2,
        "transfer_status": "Scheduled",
        "created_at": "2025-12-02T15:28:59Z",
        "updated_at": "2025-12-04T11:14:38Z",
        "items": [{"item_id": "1", "amount": 5}]
    }

    # Send a POST request to the API
    response = requests.post(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 201 (Created)
    assert status_code == 201

def test_post_Transfer2018GetsAddedWithHalfBody(_data):
    url = _data['url'] + 'transfers'

    body = {
        "id": 2018,
        "reference": "TRF-002018",
        "from_location_id": 1,
    }

    # Send a POST request to the API
    response = requests.post(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 400 (Bad Request)
    assert status_code == 400


def test_get_ReturnsItemsInTransfer2016(_data):
    url = _data['url'] + 'transfers/2016/items'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    # Get the status code and response data
    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200

def test_get_ReturnsItemsInNonExistentTransfer10000(_data):
    url = _data['url'] + 'transfers/10000/items'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    # Get the status code and response data
    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404


def test_put_UpdatesTransfer2016WithFullBody(_data):
    transfer_id = 2016
    url = _data['url'] + f'transfers/{transfer_id}'

    # Data om de transfer mee te updaten
    body = {
        "id": transfer_id,
        "reference": "TRF-002016",
        "from_location_id": 1,
        "to_location_id": 3,
        "transfer_status": "Scheduled",
        "created_at": "2025-12-02T15:28:59Z",
        "updated_at": "2025-12-05T11:14:38Z",
        "items": [{"item_id": "1", "amount": 5}]
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200

def test_put_UpdatesNonExistentTransfer10000WithFullBody(_data):
    transfer_id = 10000
    url = _data['url'] + f'transfers/{transfer_id}'

    # Data om de transfer mee te updaten
    body = {
        "id": transfer_id,
        "reference": "TRF-010000",
        "from_location_id": 1,
        "to_location_id": 3,
        "transfer_status": "Scheduled",
        "created_at": "2025-12-02T15:28:59Z",
        "updated_at": "2025-12-05T11:14:38Z",
        "items": [{"item_id": "1", "amount": 5}]
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404

def test_put_UpdatesTransfer2016WithHalfBody(_data):
    transfer_id = 2016
    url = _data['url'] + f'transfers/{transfer_id}'

    # Data om de transfer mee te updaten
    body = {
        "id": transfer_id,
        "reference": "TRF-002016",
        "from_location_id": 1,
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 400 (Bad Request)
    assert status_code == 400


def test_put_CommitsTransfer2016(_data):
    transfer_id = 2016
    url = _data['url'] + f'transfers/{transfer_id}/commit'

    # Send a PUT request to the API
    response = requests.put(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200

def test_put_CommitsNonExistentTransfer10000(_data):
    transfer_id = 10000
    url = _data['url'] + f'transfers/{transfer_id}/commit'

    # Send a PUT request to the API
    response = requests.put(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404

def test_put_CommitsAlreadyProcessedTransfer2016(_data):
    transfer_id = 2016
    url = _data['url'] + f'transfers/{transfer_id}/commit'

    # Send a PUT request to the API
    response = requests.put(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 400 (Bad Request)
    assert status_code == 400


def test_delete_DeletesTransfer2016(_data):
    transfer_id = 2016
    url = _data['url'] + f'transfers/{transfer_id}'

    # Send a DELETE request to the API
    response = requests.delete(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200

def test_delete_DeletesNonExistentTransfer10000(_data):
    transfer_id = 10000
    url = _data['url'] + f'transfers/{transfer_id}'

    # Send a DELETE request to the API
    response = requests.delete(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404