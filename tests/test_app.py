import json
from app import app


def test_fetch_data():
    client = app.test_client()
    response = client.get('/data')

    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert 'temperature' in data[0]
