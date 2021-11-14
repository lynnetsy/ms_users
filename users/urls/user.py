from users import app
from users.controllers import userController


@app.route('/')
def list():
    return userController.list()


@app.route('/', methods=['POST'])
def create():
    return userController.create()


@app.route('/<id>')
def detail(id):
    return userController.detail(id)


@app.route('/<id>', methods=['PUT'])
def update(id):
    return userController.update(id)


@app.route('/<id>', methods=['DELETE'])
def delete(id):
    return userController.delete(id)
