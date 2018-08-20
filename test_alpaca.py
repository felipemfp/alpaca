import os
import tempfile
import pytest

from alpaca import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    client.post('__clear')

    yield client


def test_empty_list(client):
    rv = client.get('/__list')
    json_data = rv.get_json()

    assert json_data == []

def test_get_returning_json(client):
    rv = client.post('/__setup/test?method=GET&status=200&Content-Type=application/json', json={
        'hello': 'world',
    })

    assert rv.status_code == 204

    res = client.get('/test')

    assert res.status_code == 200
    assert res.headers['Content-type'] == 'application/json'

    json_data = res.get_json()

    assert json_data == {'hello': 'world'}

def test_post_returning_json(client):
    rv = client.post('/__setup/test?method=POST&status=200&Content-Type=application/json', json={
        'hello': 'world',
        'post': True,
    })

    assert rv.status_code == 204

    res = client.post('/test')

    assert res.status_code == 200
    assert res.headers['Content-type'] == 'application/json'

    json_data = res.get_json()

    assert json_data == {
            'hello': 'world',
            'post': True
        }

def test_delete_returning_json(client):
    rv = client.post('/__setup/test?method=DELETE&status=200&Content-Type=application/json', json={
        'hello': 'world',
        'delete': True,
    })

    assert rv.status_code == 204

    res = client.delete('/test')

    assert res.status_code == 200
    assert res.headers['Content-type'] == 'application/json'

    json_data = res.get_json()

    assert json_data == {
            'hello': 'world',
            'delete': True
        }

def test_put_returning_json(client):
    rv = client.post('/__setup/test?method=PUT&status=200&Content-Type=application/json', json={
        'hello': 'world',
        'put': True,
    })

    assert rv.status_code == 204

    res = client.put('/test')

    assert res.status_code == 200
    assert res.headers['Content-type'] == 'application/json'

    json_data = res.get_json()

    assert json_data == {
            'hello': 'world',
            'put': True
        }