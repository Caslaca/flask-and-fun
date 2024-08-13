"""
This module contains the factory function for creating a Flask application instance.
"""

import os
from flask import Flask

def create_app():
    """
    Create and configure the Flask application.

    Returns:
        app (Flask): The Flask application instance.
    """
    app = Flask(__name__)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def hello():
        """
        A simple route that returns a greeting.

        Returns:
            str: A greeting message.
        """
        return "Hello, World v3"

    return app
