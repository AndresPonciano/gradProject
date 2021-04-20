"""
Module Docstring Goes Here
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """
    Function Docstring Goes Here
    """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)


    with app.app_context():
        from . import models

        db.create_all()
        return app
