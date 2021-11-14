from flask import json
from fixture import app, client
from users.repositories import userRepo


def test_index(client):
    res = client.get('/about')
    data = json.loads(res.data)
    assert res.status_code == 200
    assert res.content_type == 'application/json'
    assert list(data.keys()) == ['code', 'data']

def test_user_list(client):
    res = client.get('/')
    assert res.status_code == 200

def test_user_create(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    res = client.post('/', data=data)
    assert res.status_code == 200

def test_user_detail(client):
    res = client.get('/1')
    assert res.status_code == 200

def test_user_update(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret',
    }
    user = userRepo.add(data)
    new_data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe.00@example.com',
        'phone': '1231231231',
    }
    res = client.put(f'/{user.id}', data=new_data)
    assert res.status_code == 200

def test_user_delete(client):
    res = client.delete('/1')
    assert res.status_code == 200
