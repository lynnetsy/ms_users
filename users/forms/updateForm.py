from wtforms import StringField
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    Regexp
)
from users.models import User
from users.helpers.regex import username_regex, phone_regex, password_regex
from users.forms.validators.unique import Unique
from .form import FormRequest


class UpdateForm(FormRequest):
    def rules(self, request) -> dict:
        user_id = request.view_args.get('id')

        return {
            'username': StringField('username', validators=[
                DataRequired(),
                Length(min=4, max=60),
                Regexp(username_regex, message='The username is invalid'),
                Unique(User, except_id=user_id)
            ]),
            'email': StringField('email', validators=[
                DataRequired(),
                Email(),
                Length(max=255),
                Unique(User, except_id=user_id),
            ]),
            'phone': StringField('phone', validators=[
                DataRequired(),
                Length(min=9, max=15),
                Regexp(phone_regex, message='The phone is invalid'),
                Unique(User, except_id=user_id),
            ]),
            'name': StringField('name', validators=[
                Length(max=50),
            ]),
            'lastname': StringField('lastname', validators=[
                Length(max=50),
            ])
        }
