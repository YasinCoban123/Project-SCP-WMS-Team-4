import pytest
import requests


@pytest.fixture
def _data():
    return {
        'url': 'http://localhost:3000/api/v1/',
        'api_key': 'f4a5c6i7l8i9t0y1m2a3n4a5g6',
    }


def test_get_ReturnAllWarehouses(_data):
    url = _data['url'] + 'warehouses'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    # Get the status code and response data
    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200

def test_get_ReturnsWarehouse10000(_data):
    url = _data['url'] + 'warehouses/10000'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    # Get the status code and response data
    status_code = response.status_code

    # Verify that the status code is 404 (Bad Request)
    assert status_code == 404

def test_get_ReturnsWarehouse10(_data):
    url = _data['url'] + 'warehouses/10'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    # Get the status code and response data
    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_post_Warehouse2016GetsAddedWithFullBody(_data):
    url = _data['url'] + 'warehouses'

    body = {
            "id": "2016",
            "code": "JUR-NNN",
            "name": "Jumbo DC Hal reference",
            "address": "De Wijnhaven 409",
            "city": "Rotterdam",
            "zip_code": "1111 OP",
            "province": "Midden-Brabant",
            "country": "Bali",
            "contact_name": "Ali gewoon Ali",
            "contact_phone": "(032) 1819600",
            "contact_email": "vgh-amb@jumbo-logistiek.nl",
            "created_at": "2026-06-21T22:43:23Z",
            "updated_at": "2027-06-23T04:51:45Z"
        }

    # Send a POST request to the API
    response = requests.post(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 201 (Created)
    assert status_code == 201

def test_post_Warehouse2018GetsAddedWithHalfBody(_data):
    url = _data['url'] + 'warehouses'

    body = {
            "id": "2018",
            "code": "JUR-NNN",
            "name": "Jumbo DC Hal reference",
            "address": "De Wijnhaven 409",
            "city": "Rotterdam",
            "zip_code": "1111 OP",
            "province": "Midden-Brabant",
        }

    # Send a POST request to the API
    response = requests.post(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 201 (Created)
    assert status_code == 400


def test_put_UpdatesWarehouse1WithFullBody(_data):
    warehouse_id = 1
    url = _data['url'] + f'warehouses/{warehouse_id}'

    # Data om het warehouse mee te updaten
    body ={
        "id": warehouse_id,
        "code": "VGH-AMB",
        "name": "Jumbo DC Hal reference",
        "address": "De Amert 409",
        "city": "Veghel",
        "zip_code": "5462 GH",
        "province": "Noord-Brabant",
        "country": "Netherlands",
        "contact_name": "Ali Schellekens",
        "contact_phone": "(032) 1819600",
        "contact_email": "vgh-amb@jumbo-logistiek.nl",
        "created_at": "2024-06-21T22:43:23Z",
        "updated_at": "2024-06-23T04:51:45Z"
    }

def test_put_UpdatesNonExistentWarehouse1000WithFullBody(_data):
    warehouse_id = 1000
    url = _data['url'] + f'warehouses/{warehouse_id}'

    # Data om het warehouse mee te updaten
    body ={
        "id": warehouse_id,
        "code": "VGH-AMB",
        "name": "Jumbo DC Hal reference",
        "address": "De Amert 409",
        "city": "Veghel",
        "zip_code": "5462 GH",
        "province": "Noord-Brabant",
        "country": "Netherlands",
        "contact_name": "Ali Schellekens",
        "contact_phone": "(032) 1819600",
        "contact_email": "vgh-amb@jumbo-logistiek.nl",
        "created_at": "2024-06-21T22:43:23Z",
        "updated_at": "2024-06-23T04:51:45Z"
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200

def test_put_UpdatesWarehouse1WithHalfBody(_data):
    warehouse_id = 1
    url = _data['url'] + f'warehouses/{warehouse_id}'

    # Data om het warehouse mee te updaten
    body ={
        "id": warehouse_id,
        "code": "VGH-AMB",
        "name": "Jumbo DC Hal reference",
        "address": "De Amert 409",
        "city": "Veghel",
        "zip_code": "5462 GH",
        "province": "Noord-Brabant",
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200
    


def test_delete_DeletesWarehouse1(_data):
    warehouse_id = 1
    url = _data['url'] + f'warehouses/{warehouse_id}'

    # Send a DELETE request to the API
    response = requests.delete(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

     # Verify that the status code is 200 (OK)
    assert status_code == 200

def test_delete_DeletesNonExistentWarehouse10000(_data):
    warehouse_id = 10000 
    url = _data['url'] + f'warehouses/{warehouse_id}'

    # Send a DELETE request to the API
    response = requests.delete(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

     # Verify that the status code is 404 (Bad Request)
    assert status_code == 404

    