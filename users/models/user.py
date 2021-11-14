import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash
from users.db import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(
        db.String(length=36),
        default=lambda: str(uuid.uuid4()),
        primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(50), nullable=True)
    lastname = db.Column(db.String(50), nullable=True)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False)
    deleted_at = db.Column(db.DateTime, default=None, nullable=True)

    _fillable = ('username', 'email', 'phone', 'name', 'lastname')

    def __init__(self, data: dict) -> None:
        self.setAttrs(data)

    def __repr__(self) -> str:
        return f'<User {self.id} {self.email}>'

    @property
    def fullname(self) -> str:
        return f'{self.name} {self.lastname}'

    def set_password(self, password: str) -> None:
        self.password = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)
