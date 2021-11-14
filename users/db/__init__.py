from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from users import app
from users.models import Model


db = SQLAlchemy(app, model_class=Model)
migrate = Migrate(app, db)
