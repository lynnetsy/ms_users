from fixture import app, client
from users.db import db
from users.models import User
from users.repositories import userRepo


def test_user_model_fullname(client):
    data = {
        'name': 'Jhon',
        'lastname': 'Doe',}
    user = User(data)
    assert user.fullname == 'Jhon Doe'

def test_user_model_setattrs(client):
    data = {
        'username': 'jhon.doe',
        'password': 'secret'}
    user = User(data)
    assert user.username == 'jhon.doe'
    assert user.password == None

def test_user_model_update(client):
    user = User({'username': 'jhon.doe.00'})
    user.update({'username': 'jhon.doe.01'})
    assert user.username == 'jhon.doe.01'

def test_user_model_setpassword(client):
    user = User({'username': 'jhon.doe'})
    user.set_password('secret')
    assert user.password is not None
    assert user.password != 'secret'
    assert user.verify_password('secret') == True
    assert user.verify_password('test') == False

def test_user_model_repr(client):
    user = User({'email': 'jhon.doe@example.com'})
    assert str(user) == '<User None jhon.doe@example.com>'

def test_user_save(client):
    data = {
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',}
    user = User(data)
    user.set_password('secret')
    assert user.id is None
    db.session.add(user)
    db.session.commit()
    assert user.id is not None

def test_user_repo_add(client):
    user = userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret', })
    assert isinstance(user, User)
    assert user.id is not None

def test_user_repo_find(client):
    user = userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret', })
    user_found = userRepo.find(user.id)
    assert isinstance(user_found, User)
    user_not_found = userRepo.find('foo')
    assert user_not_found is None

def test_user_repo_find_by_attr(client):
    user = userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret', })
    user_found = userRepo.find_by_attr('username', 'jhon.doe')
    assert isinstance(user_found, User)

def test_user_repor_find_optional(client):
    user = userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret', })
    user_found = userRepo.find_optional({
        'username': 'jhon',
        'email': 'jhon.doe@example.com'})
    assert isinstance(user_found, User)
    assert user_found.email == 'jhon.doe@example.com'
    
def test_user_repo_getall(client):
    user = userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret', })
    users = userRepo.all() 
    assert isinstance(users, list)
    assert len(users) == 1 

def test_user_repo_update(client):
    user = userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret', })
    user_updated = userRepo.update(user.id, {'phone': '3213213213'})
    assert user_updated.phone == '3213213213'    

def test_user_repo_delete(client):
    user = userRepo.add({
        'username': 'jhon.doe',
        'email': 'jhon.doe@example.com',
        'phone': '1231231231',
        'password': 'secret', })
    userRepo.delete(user.id)
    user = userRepo.find(user.id)
    assert user is None
