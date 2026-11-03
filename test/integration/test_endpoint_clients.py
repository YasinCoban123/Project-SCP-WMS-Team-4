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
        'id': 9999,
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
        'id': 2,
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

    assert response.status_code == 200


def test_delete_deletes_client_6(_data):
    client_id = 6
    url = _data['url'] + f'clients/{client_id}'

    # Send a DELETE request to the API
    response = requests.delete(url, headers={'API_KEY': _data['api_key']})

    # Verify that the status code is 200 (OK)
    assert response.status_code == 200


def test_get_clients_without_api_key_returns_401(_data):
    url = _data['url'] + 'clients'

    response = requests.get(url)

    assert response.status_code == 401


def test_post_clients_without_api_key_returns_401(_data):
    url = _data['url'] + 'clients'

    response = requests.post(url, json={})

    assert response.status_code == 401


def test_post_clients_with_invalid_api_key_returns_401(_data):
    url = _data['url'] + 'clients'

    response = requests.post(url, json={}, headers={'API_KEY': 'invalid-key'})

    assert response.status_code == 401


def test_put_client_without_api_key_returns_401(_data):
    url = _data['url'] + 'clients/1'

    response = requests.put(url, json={})

    assert response.status_code == 401


def test_put_client_with_invalid_api_key_returns_401(_data):
    url = _data['url'] + 'clients/1'

    response = requests.put(url, json={}, headers={'API_KEY': 'invalid-key'})

    assert response.status_code == 401


def test_delete_client_without_api_key_returns_401(_data):
    url = _data['url'] + 'clients/1'

    response = requests.delete(url)

    assert response.status_code == 401


def test_delete_client_with_invalid_api_key_returns_401(_data):
    url = _data['url'] + 'clients/1'

    response = requests.delete(url, headers={'API_KEY': 'invalid-key'})

    assert response.status_code == 401


def test_get_clients_with_invalid_api_key_returns_401(_data):
    url = _data['url'] + 'clients'

    response = requests.get(url, headers={'API_KEY': 'invalid-key'})

    assert response.status_code == 401


def test_post_client_route_without_api_key_returns_401(_data):
    url = _data['url'] + 'clients/1'

    response = requests.post(url, json={})

    assert response.status_code == 401


def test_post_client_route_with_invalid_api_key_returns_401(_data):
    url = _data['url'] + 'clients/1'

    response = requests.post(url, json={}, headers={'API_KEY': 'invalid-key'})

    assert response.status_code == 401


def test_put_client_orders_without_api_key_returns_401(_data):
    url = _data['url'] + 'clients/1/orders'

    response = requests.put(url, json={})

    assert response.status_code == 401


def test_delete_unknown_client_without_api_key_returns_401(_data):
    url = _data['url'] + 'clients/10000'

    response = requests.delete(url)

    assert response.status_code == 401


def test_get_client_returns_expected_data(_data):
    response = requests.get(
        _data['url'] + 'clients/5',
        headers={'API_KEY': _data['api_key']},
    )

    assert response.status_code == 200
    client = response.json()
    assert client['id'] == 5
    assert client['name']
    assert client['contact_email']


def test_get_clients_returns_non_empty_list(_data):
    response = requests.get(
        _data['url'] + 'clients',
        headers={'API_KEY': _data['api_key']},
    )

    assert response.status_code == 200
    clients = response.json()
    assert isinstance(clients, list)
    assert clients
    assert any(client['id'] == 5 for client in clients)


def test_post_client_can_be_retrieved_after_creation(_data):
    client = {
        'id': 999901,
        'name': 'Integration client',
        'address': 'Teststraat 1',
        'city': 'Utrecht',
        'zip_code': '3511AA',
        'province': 'Utrecht',
        'country': 'Netherlands',
        'contact_name': 'Integration Tester',
        'contact_phone': '0301234567',
        'contact_email': 'integration-client@example.com',
    }

    create_response = requests.post(
        _data['url'] + 'clients',
        headers={'API_KEY': _data['api_key']},
        json=client,
    )
    get_response = requests.get(
        _data['url'] + 'clients/999901',
        headers={'API_KEY': _data['api_key']},
    )

    assert create_response.status_code == 201
    assert get_response.status_code == 200
    assert get_response.json()['name'] == client['name']
    assert get_response.json()['contact_email'] == client['contact_email']


def test_put_client_changes_persisted_data(_data):
    client = {
        'id': 2,
        'name': 'Updated integration client',
        'address': 'Nieuwe Teststraat 2',
        'city': 'Amersfoort',
        'zip_code': '3811AA',
        'province': 'Utrecht',
        'country': 'Netherlands',
        'contact_name': 'Updated Tester',
        'contact_phone': '0337654321',
        'contact_email': 'updated-client@example.com',
    }

    update_response = requests.put(
        _data['url'] + 'clients/2',
        headers={'API_KEY': _data['api_key']},
        json=client,
    )
    get_response = requests.get(
        _data['url'] + 'clients/2',
        headers={'API_KEY': _data['api_key']},
    )

    assert update_response.status_code == 200
    assert get_response.status_code == 200
    updated_client = get_response.json()
    assert updated_client['id'] == 2
    assert updated_client['name'] == client['name']
    assert updated_client['province'] == client['province']


def test_delete_client_removes_it_from_api(_data):
    client = {
        'id': 999902,
        'name': 'Client to delete',
        'address': 'Verwijderstraat 3',
        'city': 'Groningen',
        'zip_code': '9711AA',
        'province': 'Groningen',
        'country': 'Netherlands',
        'contact_name': 'Delete Tester',
        'contact_phone': '0501234567',
        'contact_email': 'delete-client@example.com',
    }

    create_response = requests.post(
        _data['url'] + 'clients',
        headers={'API_KEY': _data['api_key']},
        json=client,
    )
    delete_response = requests.delete(
        _data['url'] + 'clients/999902',
        headers={'API_KEY': _data['api_key']},
    )
    get_response = requests.get(
        _data['url'] + 'clients/999902',
        headers={'API_KEY': _data['api_key']},
    )

    assert create_response.status_code == 201
    assert delete_response.status_code == 200
    assert get_response.status_code == 404


def test_get_client_orders_returns_list(_data):
    response = requests.get(
        _data['url'] + 'clients/1/orders',
        headers={'API_KEY': _data['api_key']},
    )

    assert response.status_code == 200
    orders = response.json()
    assert isinstance(orders, list)
    assert orders
    assert all(
        1 in (
            order['client_id'],
            order['ship_to_client_id'],
            order['bill_to_client_id'],
        )
        for order in orders
    )