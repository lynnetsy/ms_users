from flask import jsonify
from users import app
from .user import *


@app.route('/about')
def app_version():
    return jsonify({
        'data': {
            'name': app.config.get('APP_NAME'),
            'version': app.config.get('APP_VERSION'),
        },
        'code': 200
    }), 200
