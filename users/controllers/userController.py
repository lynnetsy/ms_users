import uuid
from flask import jsonify, Response
from users.decorators import form_validator
from users.forms import BaseForm, CreateForm, UpdateForm


class UserController():
    def list(self) -> tuple[Response, int]:
        return jsonify({}), 200

    @form_validator(CreateForm)
    def create(self, form: BaseForm) -> tuple[Response, int]:
        return jsonify({}), 200

    def detail(self, id: uuid) -> tuple[Response, int]:
        return jsonify({}), 200

    @form_validator(UpdateForm)
    def update(self, id: uuid, form: BaseForm) -> tuple[Response, int]:
        return jsonify({}), 200

    def delete(self, id: uuid) -> tuple[Response, int]:
        return jsonify({}), 200
