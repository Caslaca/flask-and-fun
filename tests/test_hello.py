"""
This module contains tests for the main page of the Flask application.
"""

def test_main_page(client):
    """
    Test the main page of the Flask application.

    Args:
        client (FlaskClient): A test client for the Flask application.

    Asserts:
        The response data is 'Hello, World'.
    """
    response = client.get('/')
    assert response.data == b'Hello, World'