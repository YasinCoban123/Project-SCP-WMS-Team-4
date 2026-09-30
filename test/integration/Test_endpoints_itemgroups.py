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


def test_get_ReturnsAllItemGroups(_data):
    url = _data['url'] + 'item_groups'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_get_ReturnsItemGroup1(_data):
    url = _data['url'] + 'item_groups/1'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_get_ReturnsItemGroup100000(_data):
    url = _data['url'] + 'item_groups/100000'

    # Send a GET request to the API
    response = requests.get(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404


def test_get_ReturnsItemGroupsWithoutApiKey(_data):
    url = _data['url'] + 'item_groups'

    # Send a GET request to the API without an API key
    response = requests.get(url)

    status_code = response.status_code

    # Verify that the status code is 401 (Unauthorized)
    assert status_code == 401


def test_post_ItemGroup999001GetsAddedWithFullBody(_data):
    url = _data['url'] + 'item_groups'

    body = {
        "id": 999001,
        "name": "Integration test group",
        "description": "Created by integration test",
        "created_at": "2025-08-01T15:30:26Z",
        "updated_at": "2025-08-01T15:30:26Z"
    }

    # Send a POST request to the API
    response = requests.post(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 201 (Created)
    assert status_code == 201


def test_post_ItemGroup999002GetsAddedWithHalfBody(_data):
    url = _data['url'] + 'item_groups'

    body = {
        "id": 999002,
        "name": "Integration test group half body",
    }

    # Send a POST request to the API
    response = requests.post(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 400 (Bad Request)
    assert status_code == 400


def test_put_UpdatesItemGroup1WithFullBody(_data):
    item_group_id = 1
    url = _data['url'] + f'item_groups/{item_group_id}'

    # Data to update the item group with
    body = {
        "id": item_group_id,
        "name": "over datum",
        "description": "Updated description",
        "created_at": "2025-08-01T15:30:26Z",
        "updated_at": "2025-08-02T10:00:00Z"
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_put_UpdatesItemGroup1WithHalfBody(_data):
    item_group_id = 1
    url = _data['url'] + f'item_groups/{item_group_id}'

    # Data to update the item group with
    body = {
        "id": item_group_id,
        "name": "over datum",
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_put_UpdatesItemGroup100000(_data):
    item_group_id = 100000
    url = _data['url'] + f'item_groups/{item_group_id}'

    body = {
        "id": item_group_id,
        "name": "does not exist",
        "description": "Updated description",
    }

    # Send a PUT request to the API
    response = requests.put(url, json=body, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404


def test_delete_DeletesItemGroup999001(_data):
    item_group_id = 999001
    url = _data['url'] + f'item_groups/{item_group_id}'

    # Send a DELETE request to the API
    response = requests.delete(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 200 (OK)
    assert status_code == 200


def test_delete_DeletesItemGroup100000(_data):
    item_group_id = 100000
    url = _data['url'] + f'item_groups/{item_group_id}'

    # Send a DELETE request to the API
    response = requests.delete(url, headers={'API_KEY': _data['api_key']})

    status_code = response.status_code

    # Verify that the status code is 404 (Not Found)
    assert status_code == 404