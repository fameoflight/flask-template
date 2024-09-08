import pytest
from flask_template.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}


def test_data_endpoint(client):
    response = client.get('/api/data')
    assert response.status_code == 200
    assert response.json == {"data": [1, 2, 3, 4, 5]}
