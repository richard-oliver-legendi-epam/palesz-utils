def test_index(client):
    response = client.get('/')
    assert b'Kalkul\xc3\xa1torok' in response.data
