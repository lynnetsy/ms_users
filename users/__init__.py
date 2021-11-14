from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import users.config
import users.commands
import users.urls
import users.models

