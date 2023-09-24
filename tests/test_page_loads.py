def test_index(client):
    assert client.get('/').status_code == 200


def test_dilution(client):
    assert client.get('/dilution').status_code == 200


def test_separation(client):
    assert client.get('/separation').status_code == 200
