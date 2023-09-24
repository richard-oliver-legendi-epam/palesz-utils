def test_separation(client):
    response = client.get('/separation')
    assert b'Az el\xc5\x91p\xc3\xa1rlatra vonatkoz\xc3\xb3 mennyis\xc3\xa9gek:' in response.data
