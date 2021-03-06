import os

from flask import Flask
from flask_cors import CORS, cross_origin
from sqlalchemy.ext.automap import automap_base


from . import extensions, resources


def create_app(environment='dev'):
    app = Flask('proxy-resource-server')
    app.config['DEBUG'] = True
    CORS(app)

    app.config.from_pyfile('config/{}.py'.format(environment))

    extensions.db.init_app(app)
    extensions.api.init_app(app)
    with app.app_context():
        extensions.db.create_all()
        db_mappings.map_existing_tables()
        

    return app
