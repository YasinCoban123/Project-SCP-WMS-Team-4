import pytest
import requests


@pytest.fixture
def _data():
    return {
        'url': 'http://localhost:3000/api/v1/',
        'api_key': 'f4a5c6i7l8i9t0y1m2a3n4a5g6',
    }


def test_get_ReturnAllLocations(_data):
    url = _data['url'] + 'locations'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    # Get the status code and response data
    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200

def test_get_ReturnsLocation10000(_data):
    url = _data['url'] + 'locations/10000'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    # Get the status code and response data
    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404

def test_get_ReturnsLocation10(_data):
    url = _data['url'] + 'locations/10'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    # Get the status code and response data
    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200

def test_get_ReturnsLocationsInWarehouse1(_data):
    url = _data['url'] + 'warehouses/1/locations'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    # Get the status code and response data
    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_post_Location2016GetsAddedWithFullBody(_data):
    url = _data['url'] + 'locations'

    body = {
        "id": 2016,
        "warehouse_id": 1,
        "code": "VGH-AMB-Z99-R9-B9",
        "name": "Zone Z Aisle 99 Rack 9 Bin 9",
        "created_at": "2025-06-21T22:43:23Z",
        "updated_at": "2025-06-23T04:51:45Z"
    }

    # Send a POST request to the API
    response = requests.post(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 201 (Created)
    assert status_code == 201

def test_post_Location2018GetsAddedWithHalfBody(_data):
    url = _data['url'] + 'locations'

    body = {
        "id": 2018,
        "warehouse_id": 1,
        "code": "VGH-AMB-Z98-R9-B9",
    }

    # Send a POST request to the API
    response = requests.post(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 400 (Bad Request)
    assert status_code == 400


def test_put_UpdatesLocation2016WithFullBody(_data):
    location_id = 2016
    url = _data['url'] + f'locations/{location_id}'

    # Data om de locatie mee te updaten
    body = {
        "id": location_id,
        "warehouse_id": 1,
        "code": "VGH-AMB-Z99-R9-B9",
        "name": "Zone Z Aisle 99 Rack 9 Bin 9 updated",
        "created_at": "2025-06-21T22:43:23Z",
        "updated_at": "2025-07-23T04:51:45Z"
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200

def test_put_UpdatesNonExistentLocation1000WithFullBody(_data):
    location_id = 10000
    url = _data['url'] + f'locations/{location_id}'

    # Data om de locatie mee te updaten
    body = {
        "id": location_id,
        "warehouse_id": 1,
        "code": "VGH-AMB-X00-R0-B0",
        "name": "Bestaat niet",
        "created_at": "2025-06-21T22:43:23Z",
        "updated_at": "2025-07-23T04:51:45Z"
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404

def test_put_UpdatesLocation2016WithHalfBody(_data):
    location_id = 2016
    url = _data['url'] + f'locations/{location_id}'

    # Data om de locatie mee te updaten
    body = {
        "id": location_id,
        "warehouse_id": 1,
        "code": "VGH-AMB-Z99-R9-B9",
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 400 (Bad Request)
    assert status_code == 400


def test_delete_DeletesLocation2016(_data):
    location_id = 2016
    url = _data['url'] + f'locations/{location_id}'

    # Send a DELETE request to the API
    response = requests.delete(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200

def test_delete_DeletesNonExistentLocation10000(_data):
    location_id = 10000
    url = _data['url'] + f'locations/{location_id}'

    # Send a DELETE request to the API
    response = requests.delete(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404