import pytest
import requests


@pytest.fixture
def _data():
    return {
        'url': 'http://localhost:3000/api/v1/',
        'api_key': 's1h3i5p7p9i2n4g6s8t',
    }

def test_get_returns_client_5(_data):
    url = _data['url'] + 'clients/5'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    # Get the status code and response data
    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_post_adds_client(_data):
    url = _data['url'] + 'clients'
    client = {
        'name': 'Jumbo Marum Chloehof de POST heeft gewerkt',
        'address': 'Marijnboulevard 90',
        'city': 'Marum',
        'zip_code': '2005 TA',
        'province': 'Overijssel',
        'country': 'Netherlands',
        'contact_name': 'Noa Schroeff',
        'contact_phone': '+31(0)835-652156',
        'contact_email': 'van-de-biesenbosmadelief@bleijenberg.info',
    }

    # Send a POST request to the API
    response = requests.post(
        url,
        headers={'API_KEY': _data['api_key']},
        json=client,
    )

    # Verify that the status code is 201 (Created)
    assert response.status_code == 201


def test_put_return_updated_client_info_2(_data):
    url = _data['url'] + 'clients/2'
    client = {
        'name': 'Jumbo Amersfoort Leusderweg',
        'address': 'Leusderweg 152',
        'city': 'Amersfoort',
        'zip_code': '9704WL',
        'province': 'Drenthe put het gewerkt aan de rhijn',
        'country': 'Netherlands',
        'contact_name': 'Thomas Spruyt',
        'contact_phone': '(0252) 880957',
        'contact_email': 'heerkenssofia@koninklijke.com',
    }

    # Send a PUT request to the API
    response = requests.put(
        url,
        headers={'API_KEY': _data['api_key']},
        json=client,
    )

    assert response.status_code == 201
    assert response.json() == client


def test_delete_deletes_client_6(_data):
    client_id = 6
    url = _data['url'] + f'clients/{client_id}'

    # Send a DELETE request to the API
    response = requests.delete(url, headers={'API_KEY': _data['api_key']})

    # Verify that the status code is 200 (OK)
    assert response.status_code == 200