import abc
from flask_wtf import FlaskForm
from flask import Request
from wtforms import StringField
from wtforms.validators import DataRequired


def strip_filter(value):
    if value is not None and hasattr(value, 'strip'):
        return value.strip()
    return value


class BaseForm(FlaskForm):
    class Meta:
        def bind_field(self, form, unbound_field, options):
            filters = unbound_field.kwargs.get('filters', [])
            filters.append(strip_filter)
            return unbound_field.bind(form=form, filters=filters, **options)


class FormRequest():
    def __init__(self, data: dict, request: Request) -> None:
        self.data = data
        self.request = request
        self.form = None

    @property
    def errors(self):
        return None if self.form is None else self.form.errors

    def validate(self):
        class Form(BaseForm):
            pass

        rules = self.rules(self.request)

        for col, rule in rules.items():
            setattr(Form, col, rule)

        self.form = Form(data=self.data, meta={'csrf': False})
        return self.form.validate()

    @abc.abstractmethod
    def rules(self, request) -> dict:
        pass
