from palesz_utils import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_index(client):
    response = client.get('/')
    assert b'Kalkul\xc3\xa1torok' in response.data
