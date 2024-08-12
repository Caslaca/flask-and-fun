"""
This module contains pytest fixtures for testing the Flask application.
"""

import pytest
from hello import create_app

@pytest.fixture
def app():
    """
    Fixture to create and configure a new app instance for each test.

    Yields:
        Flask: The Flask application instance.
    """
    app_instance = create_app()
    yield app_instance

@pytest.fixture
def client(app):
    """
    Fixture to create a test client for the app.

    Args:
        app (Flask): The Flask application instance.

    Returns:
        FlaskClient: A test client for the Flask application.
    """
    return app.test_client()